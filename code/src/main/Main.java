package main;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

import data.Game;

public class Main {
    static int safetyNumber = 0;
    public static void main(String[] args) throws Exception {

        writeContent("Hallo,\nwillkommen im Textgame\ndas Spiel spielt komplett in einem Textdokument...\nfalls es dir noch nicht aufgefallen ist.\n\nschreibe deine Antwort einfach in die nächste Zeile\nin der Textdatei und drücke Ctrl + S\nfangen wir an, wie willst du genannt werden:");

        long lastTime = System.nanoTime();
        double nsPerUpdate = 1000000000.0 / 5.0; // 60 Updates pro Sekunde
        double delta = 0.0;
        
        while (true) {
            long now = System.nanoTime();
            delta += (now - lastTime) / nsPerUpdate;
            lastTime = now;
            
            if (delta >= 1.0) {
                System.out.println(readAnswer());
                if (readAnswer() != null) {
                    Game.userName = readAnswer();
                    writeContent("hallo " + Game.userName + ", schön, dass du dich für das Spiel entschieden hast");
                } // Hier erfolgt die Aktualisierung des Spiels
                delta--;
            }
        }
    }
    public static void writeContent(String text) {
        try {
            BufferedWriter write = new BufferedWriter(new FileWriter("test.txt", false));
            int numberOfLines = text.split("\n").length;
            write.write(text);
            write.newLine();
            write.close();
            Game.lastLine = text.split("\n")[numberOfLines - 1];
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static String readAnswer() {
        StringBuilder content = new StringBuilder();
        try {
            BufferedReader read = new BufferedReader(new FileReader("test.txt"));
            String line;
            while ((line = read.readLine()) != null) {
                content.append(line).append("\n");
            }
            read.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        String[] result = content.toString().split("\n");
        for (int i = result.length - 1; i > 0; i--) {
            if (result[i] != "") {
                if (result[i].equals(Game.lastLine)) {
                    return null;
                } else {
                    return result[i];
                }
            }
        }
        return null;
    }
}
