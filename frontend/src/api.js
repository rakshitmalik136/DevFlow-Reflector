export function fetchData() {
    // TODO: Implement API calls to backend
    return fetch('/api/data').then(response => response.json());
}
