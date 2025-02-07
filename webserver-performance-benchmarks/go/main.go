package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

type GraphRequestId struct {
	GraphName string `json: "graphName"`
}

// getAlbums responds with the list of all albums as JSON.
func test(c *gin.Context) {
	jsonData, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	var graphRequest GraphRequestId
	if err := json.Unmarshal(jsonData, &graphRequest); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	fmt.Println(graphRequest)
	c.JSON(200, gin.H{
		"graphName": graphRequest.GraphName,
	})
}

func ping(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"message": "pong",
	})
}

func main() {
	router := gin.Default()
	router.POST("/test", test)
	// Define a GET route
	router.GET("/ping", ping)
	router.Run("localhost:8080")
}
