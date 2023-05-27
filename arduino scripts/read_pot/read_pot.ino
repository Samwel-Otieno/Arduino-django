
int led=3;
float pot=A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  pinMode(pot,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  stream();

}

void stream(){
  delay(5000);
  float sensorvalue= analogRead(pot);
  Serial.println(sensorvalue);
  delay(500);
  if (sensorvalue >= 500 ){
    digitalWrite(led, HIGH);
    delay(500);
    }
  else{
    digitalWrite(led, LOW);
  }
}