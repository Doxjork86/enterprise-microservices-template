# 🚀 Enterprise Microservices Template

Plantilla de infraestructura profesional para aplicaciones web, implementando una arquitectura de microservicios segura, escalable y optimizada.

## 🏗️ Arquitectura

Este proyecto simula un entorno de producción real utilizando:

* **Nginx (Reverse Proxy):** Punto de entrada único, manejo de estáticos y enrutamiento.
* **Python (Flask + Gunicorn):** API Backend servida por un servidor WSGI de producción.
* **PostgreSQL:** Base de datos relacional aislada en red privada.
* **Docker Compose:** Orquestación de servicios y redes.
* **GitHub Actions:** Pipeline de CI/CD automatizado para construcción y publicación de imágenes.

## ⚡ Características Técnicas

* ✅ **Multi-Stage Builds:** Imágenes de Docker optimizadas (Reducción de tamaño >70%).
* ✅ **Seguridad:** Gestión de secretos vía `.env` y ejecución con usuarios no-root.
* ✅ **Resiliencia:** Implementación de `Healthchecks` nativos y auto-curación.
* ✅ **Redes Seguras:** Segregación de tráfico público vs. privado.

## 🛠️ Cómo desplegar (Local)

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Doxjork86/enterprise-microservices-template.git](https://github.com/Doxjork86/enterprise-microservices-template.git)
   cd enterprise-microservices-template

## 🤖 CI/CD Automatizado

Cada vez que subo código a la rama `main`, GitHub Actions automáticamente:
1. Construye la imagen optimizada del backend.
2. La sube a Docker Hub en: `doxjork86/enterprise-backend`.

---
*Proyecto realizado como parte del Portfolio de Ingeniería DevOps de Aliexer.R.Rosabal.*
