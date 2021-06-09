#include <SoftwareSerial.h>
String readStrings="0,0,0,0,0";
int f=0;
#define rxPin A1
#define txPin A0
SoftwareSerial mySerial(rxPin, txPin); // RX, TX
char myChar; 
void setup() {
  Serial.begin(57600);   
  mySerial.begin(9600);

}

void loop(){
  while(mySerial.available()){
    if(f==0){
      readStrings="";
      f=1;
    }
    myChar = mySerial.read();
    
     readStrings += myChar;
    //Serial.print(myChar);  
  }
  f=0;
  Serial.println(readStrings);  
  delay(80);
}
