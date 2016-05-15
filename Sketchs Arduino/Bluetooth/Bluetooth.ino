/*   ACENDENDO 2 LEDS VIA COMUNICACAO SERIAL
 AUTOR: Italo G. S. Fernandes
 DESCRICAO: Envie 'a' para alterar o estado do led1, 
 envie 'b' para alterar o estado do led2,
 O sinal devera ser enviado via comunicaçao serial.
 Programa feito para testes de comunicacao bluetooth
 */
#define pinoLed1 5
#define pinoLed2 6
boolean stateLed1 = LOW;
boolean stateLed2 = LOW;
char sinalLido;
void setup(){
  Serial.begin(9600); //Baudrate = 9600
  pinMode(pinoLed1, OUTPUT);
  pinMode(pinoLed2, OUTPUT); //definindo pinos como saidas
}

void loop(){
  if(Serial.available()){
    sinalLido = Serial.read();

    analisarSinal(sinalLido); 
  }
  delay(100);
}

void analisarSinal(char sinal){
  switch(sinal){
  case 'a':
    stateLed1 = !stateLed1;
    break;
  case 'b':
    stateLed2 = !stateLed2;
    break;
  default:
    Serial.println("Sinal nao reconhecido!");
  } 
  atualizarLeds(); 
}


void atualizarLeds(){
  digitalWrite(pinoLed1, stateLed1);
  digitalWrite(pinoLed2, stateLed2);
}


