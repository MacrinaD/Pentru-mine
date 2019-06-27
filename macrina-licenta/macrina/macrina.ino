
#define trigPin 9
#define echoPin 8
float duration, distance;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
 

}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance= (duration/2)*0.0343;
  
  Serial.print("Stare parcare:  ");
  if (distance >=400 || distance <=2) {
    Serial.println(" Parcare Goala");
  }
  else
  {
    Serial.print(distance);
    Serial.println(" cm,deci parcare ocupata!");
    delay(500);
  }
  delay(500);
 }
