---
name: audit-offer
description: Audita una oferta para encontrar puntos débiles y obtener correcciones específicas. Úsala cuando una oferta no convierte, las conversiones son bajas o algo se siente mal. Analiza el resultado soñado, la probabilidad percibida, la demora, el esfuerzo, el encaje con el mercado, el stack de valor, los precios, los mensajes y las objeciones con el framework de la Ecuación de Valor de Hormozi.
---

# Skill: Auditoría de la oferta (Detector de puntos débiles)

## Propósito
Analiza cualquier oferta e identifica qué le impide convertir.

Esta skill:
- encuentra puntos débiles
- diagnostica por qué la oferta rinde por debajo de lo esperado
- sugiere correcciones claras y prácticas

Meta: convertir una oferta débil o promedio en una compra fuerte y obvia.

---

## Cuándo usarla
Activa esta skill cuando:
- una oferta no vende
- las conversiones son bajas
- la retroalimentación es poco clara o vaga
- algo se siente “mal” pero no sabes qué
- quieres mejorar una oferta existente

---

## Entradas
Esta skill funciona con:
- un `OFFER.md`
- una página de ventas
- un pitch
- la descripción de un producto o servicio
- precios y stack de valor
- la descripción de la audiencia

---

## Resultado principal
El asistente produce:
- un diagnóstico completo de la oferta
- una lista de puntos débiles
- el nivel de severidad de cada problema
- correcciones específicas
- un plan de acción priorizado

---

## Framework de auditoría (basado en Hormozi)

La auditoría se basa en:

- Resultado soñado
- Probabilidad percibida
- Demora
- Esfuerzo y sacrificio

Además:
- claridad del mercado
- claridad de la oferta
- modelo de entrega
- stack de valor
- precios
- mensajes

---

## Comportamiento del asistente

### 1. Extrae la oferta
Identifica:
- para quién es
- qué promete
- cómo funciona
- precio
- formato

Resume:

> Esta oferta ayuda a X a lograr Y usando Z.

---

### 2. Evalúa el resultado soñado
Revisa:
- ¿el resultado es claro?
- ¿es específico?
- ¿es deseable?
- ¿es urgente?

Señales de debilidad:
- resultados vagos (“crecer”, “mejorar”)
- sin resultado medible

---

### 3. Evalúa la probabilidad percibida
Revisa:
- ¿hay pruebas?
- ¿el camino es claro?
- ¿es creíble?

Señales de debilidad:
- sin testimonios
- proceso poco claro
- promesas grandes sin respaldo

---

### 4. Evalúa la demora
Revisa:
- qué tan rápido llegan los resultados
- cuándo ocurre la primera victoria

Señales de debilidad:
- mucha demora antes de los resultados
- sin victorias rápidas

---

### 5. Evalúa el esfuerzo y el sacrificio
Revisa:
- qué tan difícil se siente
- cuántos pasos se requieren
- cuánta disciplina hace falta

Señales de debilidad:
- demasiados pasos
- instrucciones poco claras
- esfuerzo pesado

---

### 6. Evalúa el encaje con el mercado
Revisa:
- ¿la audiencia es específica?
- ¿el dolor es urgente?
- ¿pueden pagar?

Señales de debilidad:
- objetivo “todo el mundo”
- problemas de baja urgencia

---

### 7. Evalúa la estructura de la oferta
Revisa:
- ¿la oferta es fácil de entender?
- ¿la estructura es clara?
- ¿se siente completa?

Señales de debilidad:
- estructura desordenada
- componentes poco claros
- elementos faltantes

---

### 8. Evalúa el stack de valor
Revisa:
- ¿el valor se muestra con claridad?
- ¿los bonos son significativos?
- ¿hay una brecha entre el valor y el precio?

Señales de debilidad:
- bonos débiles
- sin apilado
- valor poco claro

---

### 9. Evalúa los precios
Revisa:
- ¿el precio corresponde al valor?
- ¿está justificado?
- ¿se siente barato o caro?

Señales de debilidad:
- precios al azar
- sin anclaje
- desajuste con el resultado

---

### 10. Evalúa los mensajes
Revisa:
- ¿son claros?
- ¿son específicos?
- ¿están enfocados en el resultado?

Señales de debilidad:
- lenguaje genérico
- beneficios poco claros
- sin hooks fuertes

---

### 11. Evalúa las objeciones
Revisa:
- ¿se manejan las objeciones?
- ¿se reduce el riesgo?
- ¿se construye confianza?

Señales de debilidad:
- sin garantía
- sin manejo de objeciones
- dudas sin responder

---

## Formato de salida

```md
# OFFER_AUDIT.md

## 1. Resumen de la oferta
- Para quién es
- Qué promete
- Cómo funciona
- Precio

---

## 2. Diagnóstico general
- Fortalezas
- Debilidades

---

## 3. Análisis de la Ecuación de Valor

### Resultado soñado
- Puntaje:
- Problemas:
- Correcciones:

### Probabilidad percibida
- Puntaje:
- Problemas:
- Correcciones:

### Demora
- Puntaje:
- Problemas:
- Correcciones:

### Esfuerzo y sacrificio
- Puntaje:
- Problemas:
- Correcciones:

---

## 4. Encaje con el mercado
- Problemas:
- Correcciones:

---

## 5. Estructura de la oferta
- Problemas:
- Correcciones:

---

## 6. Stack de valor
- Problemas:
- Correcciones:

---

## 7. Precios
- Problemas:
- Correcciones:

---

## 8. Mensajes
- Problemas:
- Correcciones:

---

## 9. Objeciones y confianza
- Problemas:
- Correcciones:

---

## 10. Correcciones prioritarias
1. Corrección
2. Corrección
3. Corrección

---

## 11. Victorias rápidas
- Mejoras rápidas para implementar de inmediato
```

⸻

Sistema de puntaje (opcional)

Cada categoría se puntúa en una escala 1–10:
	•	1–3 = problema crítico
	•	4–6 = necesita mejorar
	•	7–8 = sólido
	•	9–10 = fuerte

⸻

Reglas de decisión

Corrige primero el resultado cuando:
	•	no es claro
	•	no es convincente

Agrega pruebas cuando:
	•	la confianza es baja
	•	las promesas se sienten débiles

Reduce el esfuerzo cuando:
	•	la ejecución se siente pesada
	•	el abandono es alto

Reduce el tiempo cuando:
	•	los resultados se sienten lejanos
	•	la motivación es baja

Mejora los mensajes cuando:
	•	la gente no entiende rápido
	•	los hooks se sienten débiles

⸻

Ejemplo de antes vs después

Antes
	•	oferta poco clara
	•	valor débil
	•	conversiones bajas

Después
	•	resultado claro
	•	stack de valor fuerte
	•	mejor posicionamiento
	•	más conversiones

⸻

Guía de estilo
	•	directo y honesto
	•	sin relleno
	•	problemas y correcciones claros
	•	hallazgos accionables

⸻

Criterios de éxito

La skill funciona cuando:
	•	los puntos débiles son obvios
	•	las correcciones son claras y accionables
	•	la oferta se vuelve más fuerte
	•	las conversiones mejoran

