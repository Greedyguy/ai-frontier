
# Trace Sampling 2.0: Code Knowledge Enhanced Span-level Sampling for Distributed Tracing

**Korean Title:** 트레이스 샘플링 2.0: 분산 추적을 위한 코드 지식 강화된 스팬 레벨 샘플링

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Span-level Sampling|Span-level Sampling]] [[keywords/broad/Distributed Tracing|Distributed Tracing]] [[keywords/broad/Microservice Systems|Microservice Systems]] [[keywords/specific/Trace Sampling|Trace Sampling]] [[keywords/unique/Trace Sampling 2.0|Trace Sampling 2.0]] [[categories/cs.SE|cs.SE]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Span-level Sampling
**🔬 Broad Technical**: Distributed Tracing, Microservice Systems
**🔗 Specific Connectable**: Trace Sampling
**⭐ Unique Technical**: Autoscope

**ArXiv ID**: [2509.13852](https://arxiv.org/abs/2509.13852)
**Published**: 2025-09-18
**Category**: cs.SE
**PDF**: [Download](https://arxiv.org/pdf/2509.13852.pdf)


## 🏷️ 추출된 키워드



`Distributed Tracing` • 

`Microservice Systems` • 

`Trace Sampling` • 

`Autoscope` • 

`Span-level Sampling`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13852v1 Announce Type: new 
Abstract: Distributed tracing is an essential diagnostic tool in microservice systems, but the sheer volume of traces places a significant burden on backend storage. A common approach to mitigating this issue is trace sampling, which selectively retains traces based on specific criteria, often preserving only anomalous ones. However, this method frequently discards valuable information, including normal traces that are essential for comparative analysis. To address this limitation, we introduce Trace Sampling 2.0, which operates at the span level while maintaining trace structure consistency. This approach allows for the retention of all traces while significantly reducing storage overhead. Based on this concept, we design and implement Autoscope, a span-level sampling method that leverages static analysis to extract execution logic, ensuring that critical spans are preserved without compromising structural integrity. We evaluated Autoscope on two open-source microservices. Our results show that it reduces trace size by 81.2% while maintaining 98.1% faulty span coverage, outperforming existing trace-level sampling methods. Furthermore, we demonstrate its effectiveness in root cause analysis, achieving an average improvement of 8.3%. These findings indicate that Autoscope can significantly enhance observability and storage efficiency in microservices, offering a robust solution for performance monitoring.

## 🔍 Abstract (한글 번역)

arXiv:2509.13852v1 발표 유형: 새로운
요약: 분산 추적은 마이크로서비스 시스템에서 중요한 진단 도구이지만, 추적의 거대한 양은 백엔드 저장소에 상당한 부담을 줍니다. 이 문제를 완화하는 일반적인 방법은 추적 샘플링으로, 특정 기준에 따라 추적을 선택적으로 유지하며 종종 이상한 것만 보존합니다. 그러나 이 방법은 종종 비교 분석에 필수적인 정상 추적을 포함한 유용한 정보를 버립니다. 이 한계를 해결하기 위해 우리는 추적 샘플링 2.0을 소개합니다. 이는 추적 구조 일관성을 유지하면서 스팬 수준에서 작동합니다. 이 방법을 통해 모든 추적을 보존하면서 저장소 오버헤드를 크게 줄일 수 있습니다. 이 개념을 기반으로 우리는 Autoscope이라는 스팬 수준 샘플링 방법을 설계하고 구현했습니다. 이 방법은 정적 분석을 활용하여 실행 논리를 추출하여 중요한 스팬을 보존하고 구조적 무결성을 훼손하지 않습니다. 우리는 Autoscope을 두 개의 오픈 소스 마이크로서비스에서 평가했습니다. 결과는 추적 크기를 81.2% 줄이고 98.1%의 오류 스팬 커버리지를 유지함으로써 기존의 추적 수준 샘플링 방법을 능가한다는 것을 보여줍니다. 더 나아가, 우리는 Autoscope의 원인 분석에서의 효과를 증명하여 평균적으로 8.3%의 향상을 달성했습니다. 이 결과는 Autoscope이 마이크로서비스에서 관측 가능성과 저장 효율성을 크게 향상시킬 수 있으며 성능 모니터링에 대한 견고한 솔루션을 제공할 수 있다는 것을 보여줍니다.

## 📝 요약

분산 추적은 마이크로서비스 시스템에서 중요한 진단 도구이지만 추적 데이터의 양이 많아 백엔드 저장소에 부담을 줍니다. 이 문제를 완화하기 위한 일반적인 방법은 추적 샘플링인데, 이는 특정 기준에 따라 추적을 선택적으로 보관하며 종종 이상한 추적만 보존합니다. 그러나 이 방법은 종종 중요한 정보인 비정상적인 추적을 포함한 모든 추적을 버리는 문제가 있습니다. 이 한계를 해결하기 위해 우리는 추적 샘플링 2.0을 소개합니다. 이 방법은 스팬 수준에서 작동하면서 추적 구조의 일관성을 유지합니다. 이 개념을 기반으로 실행 논리를 추출하기 위해 정적 분석을 활용하는 스팬 수준 샘플링 방법인 Autoscope를 설계하고 구현했습니다. Autoscope를 두 개의 오픈 소스 마이크로서비스에서 평가했고, 결과는 추적 크기를 81.2% 줄이면서 98.1%의 오류 스팬을 보존하는 것을 보여주었습니다. 이로써 Autoscope는 마이크로서비스에서 관측성과 저장 효율성을 크게 향상시킬 수 있음을 입증하며 성능 모니터링에 대한 견고한 해결책을 제공합니다.

## 🎯 주요 포인트


- 분산 추적은 마이크로서비스 시스템에서 중요한 진단 도구이지만 추적 데이터의 양이 백엔드 저장소에 상당한 부담을 줍니다.

- Trace Sampling 2.0은 모든 추적을 유지하면서 저장소 오버헤드를 크게 줄이는 방법을 제시합니다.

- Autoscope는 실행 논리를 추출하기 위해 정적 분석을 활용하는 span-level 샘플링 방법으로, 기존의 trace-level 샘플링 방법을 능가합니다.


---

*Generated on 2025-09-18 17:22:48*