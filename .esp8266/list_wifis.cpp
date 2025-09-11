#include <ESP8266WiFi.h>

void setup() {
  Serial.begin(9600);
  delay(1000);

  Serial.println("🔎 Procurando redes WiFi...");

  // Faz uma varredura
  int n = WiFi.scanNetworks();
  Serial.println("Varredura concluída!");

  if (n == 0) {
    Serial.println("Nenhuma rede encontrada 😢");
  } else {
    Serial.printf("Foram encontradas %d redes:\n", n);
    for (int i = 0; i < n; i++) {
      // Mostra SSID, intensidade do sinal e se é aberta ou com senha
      Serial.printf("%d: %s (%d dBm)%s\n", 
        i + 1,
        WiFi.SSID(i).c_str(),
        WiFi.RSSI(i),
        (WiFi.encryptionType(i) == ENC_TYPE_NONE) ? " 🔓" : " 🔒"
      );
      delay(10);
    }
  }
}

void loop() {
  // Não precisa de nada aqui
}
