package com.thehellmaker;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

public class SerialClient {
    private final HttpClient httpClient;
    private final String url = "http://localhost:8080/ping";
    
    public SerialClient() {
        this.httpClient = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();
    }
    
    public void makeSerialRequests(int numberOfRequests) {
        try {
            long startTime = System.currentTimeMillis();
            
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();
                    
            for (int i = 0; i < numberOfRequests; i++) {
                HttpResponse<String> response = httpClient.send(request, 
                        HttpResponse.BodyHandlers.ofString());
            }
            
            long endTime = System.currentTimeMillis();
            long duration = endTime - startTime;
            System.out.println("Serial requests completed in " + duration + " ms");
            
        } catch (Exception e) {
            System.err.println("Error making requests: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        SerialClient client = new SerialClient();
        // Make 100 serial requests
        client.makeSerialRequests(Config.TOTAL_REQUESTS);
    }
}
