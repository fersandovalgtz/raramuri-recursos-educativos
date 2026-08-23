# Autoevaluación FAIR / FAIR4RS — Rarámuri · recursos educativos

Esta autoevaluación describe el estado del repositorio como **infraestructura pedagógica y software/documentación de investigación**. No constituye certificación externa ni afirma validación lingüística o comunitaria exhaustiva.

## Findable / Localizable

**Estado: medio-alto.**

- Repositorio público y versionado.
- `CITATION.cff` y `codemeta.json` proporcionan metadatos legibles por máquinas.
- ORCID del responsable identificado.
- Catálogo estructurado en `catalogo.json`.
- Falta un identificador persistente propio de versión —por ejemplo DOI de Zenodo— para cerrar la persistencia archivística de una release estable.

## Accessible / Accesible

**Estado: alto para la infraestructura publicada.**

- Código, documentación, inventarios y materiales autorizados son accesibles por HTTPS/Git.
- La política de audio exige consentimiento y la seguridad cultural limita la publicación de contenidos sensibles.
- Accesibilidad técnica no se interpreta como autorización cultural o lingüística.

## Interoperable / Interoperable

**Estado: medio-alto.**

- Metadatos en CFF y CodeMeta.
- Catálogo JSON estructurado y documentación de estados de validación.
- Relación explícita con Rarámuri Digital como infraestructura lexicográfica de origen.
- Conviene desarrollar, cuando exista suficiente corpus pedagógico publicado, esquemas machine-readable para recursos, validaciones, variantes y procedencia.

## Reusable / Reutilizable

**Estado: alto con restricciones explícitas.**

- Licencia del repositorio y estrategia de licencias documentadas.
- Separación entre datos lexicográficos y productos pedagógicos.
- Estados de validación explícitos: `draft`, `source-checked`, `technical-reviewed`, `speaker-reviewed`, `community-reviewed` y `published` sólo cuando corresponda.
- Políticas específicas para variación lingüística, audio, seguridad cultural y revisión.
- La reutilización debe conservar procedencia, atribución, variante y alcance real de la validación.

## FAIR4RS

| Dimensión | Estado | Evidencia principal |
|---|---|---|
| Identificación/versionado | medio-alto | Git, versión de infraestructura, `CHANGELOG.md`; DOI propio aún pendiente |
| Metadatos | alto | `CITATION.cff`, `codemeta.json`, README |
| Acceso | alto | GitHub/HTTPS y formatos abiertos |
| Reutilización | alto condicionado | licencia, gobernanza, validación situada y seguridad cultural |
| Reproducibilidad | medio-alto | workflow de validación y documentación estructurada |
| Procedencia | mejorado en esta revisión | `PROVENANCE.md`, políticas de fuente y validación |

## Relación entre FAIR y CARE

FAIR no es suficiente para materiales educativos vinculados con una lengua y comunidades indígenas vivas. La facilidad técnica para encontrar, descargar o reutilizar un recurso no reemplaza consideraciones de beneficio, autoridad, responsabilidad, ética, consentimiento, variación lingüística y pertinencia cultural. Por ello este repositorio mantiene las políticas de gobernanza y seguridad cultural como controles sustantivos, no decorativos.

## Brechas prioritarias

1. Publicar una primera release pedagógica estable cuando exista un conjunto suficientemente maduro y archivarla con identificador persistente.
2. Extender metadatos estructurados al nivel de cada recurso educativo y cada acto de validación.
3. Mantener visible el alcance territorial y lingüístico de las revisiones por personas hablantes.
4. Preservar resultados de revisión y corrección sin convertir una validación situada en autoridad universal.
5. Evaluar FAIR externamente sólo cuando exista un objeto archivado y citable que pueda ser sometido a una herramienta identificable.

## Política de comunicación

No utilizar `FAIR certified`, `FAIR compliant`, `community validated` ni expresiones equivalentes salvo que exista evidencia pública y verificable que sustente exactamente esa afirmación y su alcance.
