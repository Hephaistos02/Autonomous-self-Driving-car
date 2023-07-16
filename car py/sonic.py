ong Ultrasonic_read(){
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  long time = pulseIn (echo, HIGH);
  return time / 29 / 2;
}
void compareDistance(){
    if(distance_L  > distance_R){
      
       turnLeft();
      delay(700);
      forword();
      delay(600);
     
      turnRight();
      delay(900);
      forword();
      delay(500);
      turnRight();
      delay(800);
      forword();
      delay(500);
    
    }  
    
  else{
    
      turnRight();
      delay(700);
      forword();
     
      delay(600);
      turnLeft();
      delay(900);
      forword();
      delay(500);
      turnLeft();
      delay(800);
      forword();
      delay(500);
      
}
}
void Check_side(){
    Stop();
    delay(100);
 for (int angle = 70; angle <= 140; angle += 5)  {
   servoPulse(servo, angle);  }
    delay(300);
    distance_L = Ultrasonic_read();
    Serial.print("D R=");Serial.println(distance_R);
    delay(100);
  for (int angle = 140; angle >= 0; angle -= 5)  {
   servoPulse(servo, angle);  }
    delay(500);
    distance_R = Ultrasonic_read();
    Serial.print("D L=");Serial.println(distance_L);
    delay(100);
 for (int angle = 0; angle <= 70; angle += 5)  {
   servoPulse(servo, angle);  }
    delay(300);
    compareDistance();
}

void forword(){  //forword
digitalWrite(in1, HIGH); 
digitalWrite(in2, LOW);
digitalWrite(in3, HIGH); 
digitalWrite(in4, LOW); 
}

void backword(){ 
digitalWrite(in1, LOW); 
digitalWrite(in2, HIGH); 
digitalWrite(in3, LOW); 
digitalWrite(in4, HIGH); 
}

void turnRight(){ 
digitalWrite(in1, LOW); 
digitalWrite(in2, HIGH);  
digitalWrite(in3, HIGH); 
digitalWrite(in4, LOW); 
}

void turnLeft(){
digitalWrite(in1, HIGH); 
digitalWrite(in2, LOW); 
digitalWrite(in3, LOW); 
digitalWrite(in4, HIGH); 
}

void Stop(){ //stop
digitalWrite(in1, LOW); 
digitalWrite(in2, LOW);  
digitalWrite(in3, LOW);  
digitalWrite(in4, LOW);  
}