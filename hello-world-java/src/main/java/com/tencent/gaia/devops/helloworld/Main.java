package com.tencent.gaia.devops.helloworld;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class Main 
{
    public static void main(String[] arg) throws Exception {
        String weimingwu="";
        HttpServer server = HttpServer.create(new InetSocketAddress(80), 0);
        server.createContext("/", new TestHandler());
        server.start();
        System.out.println("Server start");
        System.out.println("Server is listening on port 80");
    }

    static class TestHandler implements HttpHandler{
        public void handle(HttpExchange exchange) throws IOException {
            String response = "demo http server";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
