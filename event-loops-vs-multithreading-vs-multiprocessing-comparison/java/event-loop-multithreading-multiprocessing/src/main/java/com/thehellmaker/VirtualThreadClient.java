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
import java.util.concurrent.ThreadFactory;
public class VirtualThreadClient {
    private static final AtomicInteger completedRequests = new AtomicInteger(0);
    private static long startTime;

    public static void main(String[] args) {
        startTime = System.currentTimeMillis();
        
        // Create an HttpClient with connection pooling
        HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();
        
        // Create a custom ThreadFactory to use virtual threads
        ThreadFactory virtualThreadFactory = Thread.ofVirtual().factory();
        
        // Create a virtual thread executor instead of platform thread pool
        ExecutorService executor = Executors.newFixedThreadPool(10, virtualThreadFactory);
        
        try {
            int numRequests = Config.TOTAL_REQUESTS;
            String url = "http://localhost:8080/ping";

            // Submit requests to the virtual thread executor
            for (int i = 0; i < numRequests; i++) {
                final int requestId = i;
                executor.submit(() -> makeRequest(client, url, requestId, numRequests));
            }

            // Shutdown the executor and wait for all tasks to complete
            executor.shutdown();
            if (!executor.awaitTermination(1, TimeUnit.MINUTES)) {
                executor.shutdownNow();
            }
            long endTime = System.currentTimeMillis();
            System.out.println("All " + numRequests + " requests completed in " + (endTime - startTime) + " ms");
            System.out.println("Virtual threads shut down.");
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
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
            
        } catch (Exception e) {
            System.err.println("Request " + requestId + " failed: " + e.getMessage());
        }
    }
} 