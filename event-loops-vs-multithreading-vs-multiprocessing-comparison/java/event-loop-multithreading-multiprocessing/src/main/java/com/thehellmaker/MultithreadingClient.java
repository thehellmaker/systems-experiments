package com.thehellmaker;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.TimeUnit;

public class MultithreadingClient {
    private static final AtomicInteger completedRequests = new AtomicInteger(0);
    private static long startTime;

    public static void main(String[] args) {
        startTime = System.currentTimeMillis();
        
        // Create an HttpClient with connection pooling
        HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();
                
        // Create a thread pool
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        
        int numRequests = Config.TOTAL_REQUESTS;
        String url = "http://localhost:8080/ping";

        // Submit requests to the thread pool
        for (int i = 0; i < numRequests; i++) {
            final int requestId = i;
            executor.submit(() -> makeRequest(client, url, requestId, numRequests));
        }

        // Shutdown the executor and wait for all tasks to complete
        executor.shutdown();
        try {
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
            System.err.println("Executor interrupted: " + e.getMessage());
        }
    }

    private static void makeRequest(HttpClient client, String url, int requestId, int totalRequests) {
        try {
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            // System.out.println("Request " + requestId + " completed with status: " + response.statusCode());
            
            if (completedRequests.incrementAndGet() == totalRequests) {
                long endTime = System.currentTimeMillis();
                System.out.println("All " + totalRequests + " requests completed in " + (endTime - startTime) + " ms");
                System.out.println("Threads shut down.");
            }
        } catch (Exception e) {
            // System.err.println("Request " + requestId + " failed: " + e.getMessage());
        }
    }
} 