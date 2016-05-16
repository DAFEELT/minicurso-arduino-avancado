/*   ENVIANDO DADOS DE LEITURA ANALOGICA VIA SERIAL
 AUTOR: Italo G. S. Fernandes
 DESCRICAO: Conecte algo para ser lido pela porta A0,
 O valor das leituras sera enviado via Serial
 */
 
#define pinoLeitura A0

int valorLido = 0;

void setup(){
  Serial.begin(9600);
  pinMode(pinoLeitura, INPUT);
}

void loop(){
  valorLido = analogRead(pinoLeitura);
  
  Serial.println(valorLido);  
  delay(100);
}
