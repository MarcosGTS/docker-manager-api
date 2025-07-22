import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    stages: [
        { duration: '0s', target: 0 }, // ramp-up para 100 usuários
        { duration: '1m', target: 500 }, // aumenta para 250
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95% das requisições < 500ms
        http_req_failed: ['rate<0.01'],   // menos de 1% de falhas
    }
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost:3000';

export default function () {
    // Consulta simples
    let res = http.get(`${BASE_URL}/users`);
    check(res, {
        'GET /users status 200': (r) => r.status === 200,
        'GET /users < 500ms': (r) => r.timings.duration < 500,
    });

    sleep(1);
}
