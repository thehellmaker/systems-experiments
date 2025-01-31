import http from 'k6/http';
import { check } from 'k6';

export default function () {
  const url = 'http://localhost:8080/test';
  const payload = JSON.stringify({ graphName: 'testGraph' });
  const headers = { 'Content-Type': 'application/json' };

  const response = http.post(url, payload, { headers });

  check(response, {
    'Status is 200': (r) => r.status === 200,
    'Correct JSON response': (r) => JSON.stringify(r.json()) === payload,
  });
}