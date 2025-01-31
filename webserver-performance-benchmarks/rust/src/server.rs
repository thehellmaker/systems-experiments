
pub mod http_server {
    use actix_web::{post, web, App, HttpRequest, HttpServer, Responder, Result};
    use actix_web::web::Bytes;
    use serde::{Deserialize, Serialize};

    #[derive(Deserialize, Clone, Serialize)]
    struct GraphRequestId {
        #[serde(rename = "graphName")]
        graph_name: String,
    }

    #[post("/test")]
    async fn test_api(_req: HttpRequest, bytes: Bytes) -> Result<impl Responder> {
        let graph_request_id: GraphRequestId = serde_json::from_slice(&bytes)?;
        println!("Graph Request ID: {}", graph_request_id.graph_name);
        Ok(web::Json(graph_request_id))
    }


    pub async fn start() -> std::io::Result<()> {
        HttpServer::new(|| {
            App::new()
                .service(crate::server::http_server::test_api)
        })
            .bind(("127.0.0.1", 8080))?
            .workers(10)
            .run()
            .await
    }
}

