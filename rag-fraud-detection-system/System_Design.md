System Design

This system simulates a real-time fraud detection pipeline.

Flow:
- API receives transaction
- Feature pipeline processes input
- ML model predicts fraud score
- Output returned with explanation

Scalability:
- Stateless FastAPI service
- Docker containerization
- Ready for Kubernetes deployment