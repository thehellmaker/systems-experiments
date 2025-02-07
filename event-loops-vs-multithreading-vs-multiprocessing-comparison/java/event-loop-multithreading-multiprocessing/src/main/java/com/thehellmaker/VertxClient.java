package com.thehellmaker;
import io.vertx.core.Vertx;
import io.vertx.ext.web.client.WebClient;
import io.vertx.ext.web.client.HttpResponse;

public class VertxClient {
    private static int completedRequests = 0;
    private static final Object lock = new Object();
    private static long startTime;

    public static void main(String[] args) {
        startTime = System.currentTimeMillis();
        Vertx vertx = Vertx.vertx();
        WebClient client = WebClient.create(vertx);

        int numRequests = Config.TOTAL_REQUESTS;
        String url = "http://localhost:8080/ping";  // Replace with the actual URL

        for (int i = 0; i < numRequests; i++) {
            makeRequest(client, url, i, numRequests, vertx);
        }
    }

    private static void makeRequest(WebClient client, String url, int requestId, int totalRequests, Vertx vertx) {
        client.getAbs(url).send(response -> handleResponse(response, requestId, client, totalRequests, vertx));
    }

    private static void handleResponse(io.vertx.core.AsyncResult<HttpResponse<io.vertx.core.buffer.Buffer>> response, 
            int requestId, WebClient client, int totalRequests, Vertx vertx) {
        if (response.succeeded()) {
            HttpResponse<io.vertx.core.buffer.Buffer> httpResponse = response.result();
            // System.out.println("Request " + requestId + " completed with status: " + httpResponse.statusCode());
        } else {
            // System.err.println("Request " + requestId + " failed: " + response.cause().getMessage());
        }
        
        synchronized (lock) {
            completedRequests++;
            if (completedRequests == totalRequests) {
                long endTime = System.currentTimeMillis();
                System.out.println("All " + totalRequests + " requests completed in " + (endTime - startTime) + " ms");
                client.close();
                vertx.close();
                System.out.println("Vert.x shut down.");
            }
        }
    }
}
