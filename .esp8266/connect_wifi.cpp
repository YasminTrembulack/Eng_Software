#include <ESP8266WiFi.h>  // Biblioteca Wi-Fi para ESP8266

// Coloque os dados da sua rede aqui:
const char* ssid     = "4111_Fibra";
const char* password = "sjyjeHPq";

void setup() {
  // Inicializa comunicação serial
  Serial.begin(9600);
  delay(1000);

  Serial.println("Conectando ao WiFi...");
  WiFi.begin(ssid, password);

  // Aguarda conexão
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ Conectado ao WiFi!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());  // Mostra o IP atribuído pelo roteador
}

void loop() {
  // Aqui você pode colocar qualquer lógica que use a internet
}
