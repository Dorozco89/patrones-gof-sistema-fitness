# Patrones GOF - Sistema Fitness

## Introducción

Este documento presenta el análisis conceptual de los 23 patrones de diseño GOF (Gang of Four), clasificándolos según su categoría, problema que resuelven, estructura básica, ventajas, desventajas, relaciones y posibles casos de uso dentro del desarrollo de software orientado a objetos.

El objetivo de esta documentación es servir como apoyo conceptual para la implementación práctica de patrones GOF aplicada al sistema fitness desarrollado durante la actividad académica.

---

# Tabla de Patrones GOF

| Patrón | Categoría | Problema que Resuelve | Estructura Básica | Casos de Uso | Ventajas | Desventajas | Patrones Relacionados |
|---|---|---|---|---|---|---|---|
| Abstract Factory | Creacional | Permite crear familias de objetos relacionados sin depender de clases concretas. | Cliente → Fábrica Abstracta → Productos Concretos | Sistemas con múltiples familias de objetos relacionadas, interfaces gráficas multiplataforma, creación desacoplada de componentes. | Reduce el acoplamiento, favorece la extensibilidad y consistencia entre productos. | Aumenta complejidad estructural y número de clases. | Factory Method, Builder, Singleton |
| Builder | Creacional | Permite la construción de objetos complejos paso a paso separando el proceso de construcción de la representación final. | Director → Builder → Producto | Construcción de objetos complejos, generación de configuraciones personalizadas, creación modular de estructuras. | Mejora legibilidad, desacopla construcción y facilita reutilización. | Puede aumentar la cantidad de clases y dificultad estructural. | Abstract Factory, Factory Method, Composite |
| Factory Method | Creacional | Define una interfaz para crear objetos permitiendo que las subclases decidan qué clase concreta instanciar. | Creador → Factory Method → Producto Concreto | Sistemas con múltiples tipos de objetos relacionados, creación desacoplada de componentes, frameworks extensibles. | Disminuye el acoplamiento, facilita extensión y centraliza la creación de objetos. | Puede aumentar la dificultad y cantidad de subclases. | Abstract Factory, Builder, Prototype |
