#define enA 10
#define in1 9 //Motor1  L298 Pin in1 
#define in2 8 //Motor1  L298 Pin in1 
#define in3 7 //Motor2  L298 Pin in1 
#define in4 6 //Motor2  L298 Pin in1 
#define enB 5 //Enable2 L298 Pin enB 
#define L_S A0 //ir sensor Left
#define R_S A1 //ir sensor Right
#define echo A2    //Echo pin
#define trigger A3 //Trigger pin
#define servo A5
int Set=15;
int distance_L, distance_F, distance_R; 
void setup(){ 
Serial.begin(9600);
pinMode(R_S, INPUT);   
pinMode(L_S, INPUT); 
pinMode(echo, INPUT );
pinMode(trigger, OUTPUT); 
pinMode(enA, OUTPUT); 
pinMode(in1, OUTPUT);
pinMode(in2, OUTPUT);  
pinMode(in3, OUTPUT); 
pinMode(in4, OUTPUT);
pinMode(enB, OUTPUT); 
analogWrite(enA, 150);  
analogWrite(enB, 150);
pinMode(servo, OUTPUT);
 for (int angle = 70; angle <= 140; angle += 5)  {
   servoPulse(servo, angle);  }
 for (int angle = 140; angle >= 0; angle -= 5)  {
   servoPulse(servo, angle);  }
 for (int angle = 0; angle <= 70; angle += 5)  {
   servoPulse(servo, angle);  }
distance_F = Ultrasonic_read();
delay(500);
}
void loop(){  
Serial.print("D F=");Serial.println(distance_F);
 if((digitalRead(R_S) == 0)&&(digitalRead(L_S) == 0)){
  if(distance_F > Set){forword();}
                  else{Check_side();}  
 }  


else if((digitalRead(R_S) == 1)&&(digitalRead(L_S) == 0)){turnRight();}  

else if((digitalRead(R_S) == 0)&&(digitalRead(L_S) == 1)){turnLeft();} 
    
delay(10);
}
void servoPulse (int pin,  int angle){
int pwm = (angle*11) + 500;     
 digitalWrite(pin, HIGH);
 delayMicroseconds(pwm);
 digitalWrite(pin, LOW);
 delay(50); 
}