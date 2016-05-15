using System;
using Gtk;
using System.IO.Ports;
using System.Timers;

public partial class MainWindow: Gtk.Window
{
	SerialPort minhaporta = new SerialPort ();
	Timer meutimer = new Timer ();
	public MainWindow () : base (Gtk.WindowType.Toplevel)
	{
		Build ();
		visualizador.Buffer.Text = "Status:";

		//Definições da porta serial
		minhaporta.BaudRate = 9600;
		minhaporta.Parity = Parity.None;
		minhaporta.DataBits = 8;
		minhaporta.StopBits = StopBits.One;
		minhaporta.ReadTimeout = 2;

		//Definindo timer de leitura
		meutimer.Interval = 100;
		meutimer.Elapsed += new ElapsedEventHandler (delegate {
			tick ();
		});

		listar ();
	}

	//Tenta ler a cada 100ms
	protected void tick (){
		string lido;
		try {
			lido = minhaporta.ReadLine ().ToString();
			visualizador.Buffer.Text += "\nSinal lido: " + lido;
		} catch {
			
		}
	}
		
	private void listar()
	{
		//listando as portas
		foreach (string s in SerialPort.GetPortNames())
		{
			combobox4.AppendText (s);

		}
		combobox4.Active = 0; //definindo a primeira como default
	}

	protected void OnDeleteEvent (object sender, DeleteEventArgs a)
	{
		//sempre lembre-se de fechar a porta antes de sair do programa
		if(minhaporta.IsOpen){
			minhaporta.Close();
		}
		Application.Quit ();
		a.RetVal = true;
	}

	protected void btnLED1_Clicked (object sender, EventArgs e)
	{
		//envia sinal do led1.
		if (minhaporta.IsOpen) {
			minhaporta.Write ("a");
			visualizador.Buffer.Text += "\nSinal enviado.";
		} else {
			visualizador.Buffer.Text += "\nA porta não está conectada.";
		}
			
	}

	protected void btnLED2_Clicked (object sender, EventArgs e)
	{
		//envia sinal do led2
		if (minhaporta.IsOpen) {
			minhaporta.Write ("b");
			visualizador.Buffer.Text += "\nSinal enviado.";
		} else {
			visualizador.Buffer.Text += "\nA porta não está conectada.";
		}
	}

	protected void btnConectar_Clicked (object sender, EventArgs e)
	{
		if (!minhaporta.IsOpen) {
			//define a porta a se conectar como a selecionada
			minhaporta.PortName = combobox4.ActiveText.ToString();
			visualizador.Buffer.Text += "\nConectando a " + combobox4.ActiveText;

			//tenta se conectar, caso ocorra algm erro o captura e mostra
			try {
					minhaporta.Open();
					visualizador.Buffer.Text += "\nConectado.";
					meutimer.Start ();
			} catch (Exception ex){
				visualizador.Buffer.Text += "\nNão foi possível conectar.\nErro: " + ex.Message;
			}

		} else {
			visualizador.Buffer.Text += "\nA porta já esta aberta.";
		}
	}

	protected void btnDesconectar_Clicked (object sender, EventArgs e)
	{
		//tenta se desconectar caso ocorra algum erro o captura e mostra
		try {
			if(!minhaporta.IsOpen){
				visualizador.Buffer.Text += "\nA porta já estava fechada.";
			} else {
				minhaporta.Close();
			}
			visualizador.Buffer.Text += "\nDesconectado.";
			meutimer.Stop();
		} catch (Exception ex){
			visualizador.Buffer.Text += "\nAlgo deu errado ao desconectar.\nErro: " + ex.Message;
		}
	}

}
