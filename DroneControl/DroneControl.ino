/*Serial_LED_02.ino  Arduining 4 May 2015
Controlling the LED in pin 13 with the Serial Monitor.
--- Command list: ---
? -> Print this HELP 
a -> LED On  "activate"
d -> LED Off "deactivate"
s -> LED     "status" 

Example using the switch statement.
*/
 
#define Vertical 3          
#define LeftRight 5
#define ForBack 6
#define MaxVolt  255

double upCoeff = 0.9;
double midCoeff = 0.7;
double downCoeff = 0.3;

double offCoeff =0;
double rightCoeff = 0.8;
double leftCoeff = 0.2;
double forCoeff = 0.8;
double backCoeff = 0.2;
double middle =0.5;

int delayTime = 2000;

char rxChar= 0;         // RXcHAR holds the received command.


void printHelp(void){
  Serial.println("--- Command list: ---");
  Serial.println("? -> Print this HELP");  
  Serial.println("u -> up");
  Serial.println("m -> mid");
  Serial.println("d -> down");
  Serial.println("o -> off");
  Serial.println("l -> left");  
  Serial.println("r -> right");  
  Serial.println("f -> forward");
  Serial.println("b -> back");    
  }

  
//---------------- setup ---------------------------------------------
void setup(){
  Serial.begin(9600);   // Open serial port (9600 bauds).
  pinMode(Vertical, OUTPUT); 
  pinMode(LeftRight, OUTPUT);
  pinMode(ForBack, OUTPUT);
  
  Serial.flush();       // Clear receive buffer.
  printHelp();

  delay (5000);
  analogWrite(LeftRight,0);
  analogWrite(ForBack,0);
  analogWrite(Vertical,MaxVolt);
  delay (2000);
  analogWrite(Vertical,0);
}

//--------------- loop ----------------------------------------------- 
void loop(){

  digitalWrite(LED_BUILTIN, HIGH);
  if (Serial.available() >0){          // Check receive buffer.
    rxChar = Serial.read();            // Save character received. 
    Serial.flush();                    // Clear receive buffer.
  
  switch (rxChar) {
    
    case 'u':
      analogWrite (Vertical, MaxVolt * upCoeff);
      Serial.println("up");
      break;

    case 'd':
      analogWrite (Vertical, MaxVolt * downCoeff);
      Serial.println("down");
      break;

    case 'o':
      analogWrite(Vertical, MaxVolt * offCoeff);
      Serial.println("off");
      break;

    case 'm':
      analogWrite(Vertical, MaxVolt * midCoeff);
      Serial.println("mid");
      break;

    case 'l':
      analogWrite (LeftRight, MaxVolt * leftCoeff);
      Serial.println("left");
      delay(delayTime);
      break;

    case 'r':
      analogWrite (LeftRight, MaxVolt * rightCoeff);
      Serial.println("right");
      delay(delayTime);
      break;

    case 'f':
      analogWrite (ForBack, MaxVolt * forCoeff);
      Serial.println("forward");
      delay(delayTime);
      break;
      
    case 'b':
      analogWrite (ForBack, MaxVolt * backCoeff);
      Serial.println("back");
      delay (delayTime);
      break;

    default:                           
      Serial.println("default");
      break;
    }
    
  }
  analogWrite(ForBack, MaxVolt * middle);
  analogWrite(LeftRight, MaxVolt * middle);
}
// End of the Sketch.

