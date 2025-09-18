
# Catalpa: GC for a Low-Variance Software Stack

**Korean Title:** 카탈파: 저분산 소프트웨어 스택을 위한 GC

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Tail-latencies|Tail-latencies]] [[keywords/broad/Garbage Collection|Garbage Collection]] [[keywords/broad/Runtime System|Runtime System]] [[keywords/specific/Bosque Programming Language|Bosque Programming Language]] [[keywords/unique/Catalpa Collector|Catalpa Collector]] [[categories/cs.SE|cs.SE]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Tail-latencies
**🔬 Broad Technical**: Garbage Collector, Runtime System
**🔗 Specific Connectable**: Bosque programming language
**⭐ Unique Technical**: Catalpa collector

**ArXiv ID**: [2509.13429](https://arxiv.org/abs/2509.13429)
**Published**: 2025-09-18
**Category**: cs.SE
**PDF**: [Download](https://arxiv.org/pdf/2509.13429.pdf)


## 🏷️ 추출된 키워드



`Garbage Collection` • 

`Runtime System` • 

`Bosque programming language` • 

`Catalpa collector` • 

`Tail-latencies`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13429v1 Announce Type: cross 
Abstract: The performance of an application/runtime is usually conceptualized as a continuous function where, the lower the amount of memory/time used on a given workload, then the better the compiler/runtime is. However, in practice, good performance of an application is viewed as more of a binary function - either the application responds in under, say 100 ms, and is fast enough for a user to barely notice, or it takes a noticeable amount of time, leaving the user waiting and potentially abandoning the task. Thus, performance really means how often the application is fast enough to be usable, leading industrial developers to focus on the 95th and 99th percentile tail-latencies as heavily, or moreso, than average response time. Our vision is to create a software stack that actively supports these needs via programming language and runtime system design. In this paper we present a novel garbage-collector design, the Catalpa collector, for the Bosque programming language and runtime. This allocator is designed to minimize latency and variability while maintaining high-throughput and incurring small memory overheads. To achieve these goals we leverage various features of the Bosque language, including immutability and reference-cycle freedom, to construct a collector that has bounded collection pauses, incurs fixed-constant memory overheads, and does not require any barriers or synchronization with application code.

## 🔍 Abstract (한글 번역)

arXiv:2509.13429v1 발표 유형: 교차
초록: 응용 프로그램/런타임의 성능은 일반적으로 연속 함수로 개념화되는데, 주어진 작업 부하에서 사용된 메모리/시간이 적을수록 컴파일러/런타임이 더 좋다고 여겨집니다. 그러나 실제로는 응용 프로그램의 좋은 성능은 더 이상 이진 함수로 간주됩니다 - 즉, 응용 프로그램이 100ms 미만으로 응답하고 사용자가 거의 알아채지 못할 정도로 빠르거나, 사용자가 기다리고 작업을 포기할 정도로 시간이 많이 걸리는 경우입니다. 따라서 성능이란 실제로 응용 프로그램이 사용 가능한 정도로 얼마나 자주 빠른지를 의미하며, 산업 개발자들은 평균 응답 시간보다 95번째 및 99번째 백분위수 tail-latencies에 더 많은 중점을 두거나 그 이상을 두고 있습니다. 우리의 비전은 프로그래밍 언어 및 런타임 시스템 설계를 통해 이러한 요구 사항을 적극적으로 지원하는 소프트웨어 스택을 만드는 것입니다. 본 논문에서는 Bosque 프로그래밍 언어 및 런타임을 위한 혁신적인 가비지 컬렉터 디자인 인 Catalpa 컬렉터를 제시합니다. 이 할당기는 지연 시간과 변동성을 최소화하고 높은 처리량을 유지하면서 작은 메모리 오버헤드를 발생시키도록 설계되었습니다. 이러한 목표를 달성하기 위해 Bosque 언어의 다양한 기능을 활용하여, 불변성과 참조 사이클 자유성을 포함하여, 제한된 컬렉션 일시 중지가 있는, 고정된 상수 메모리 오버헤드를 발생시키는, 응용 프로그램 코드와의 장벽이나 동기화가 필요하지 않은 컬렉터를 구축했습니다.

## 📝 요약

이 연구는 응용 프로그램/런타임의 성능을 개선하기 위해 Bosque 프로그래밍 언어 및 런타임을 위한 새로운 가비지 컬렉터인 Catalpa 컬렉터를 제안한다. Catalpa 컬렉터는 지연 시간과 변동성을 최소화하고 고 처리량을 유지하면서 작은 메모리 오버헤드를 발생시키도록 설계되었다. Bosque 언어의 다양한 기능을 활용하여 바운드된 컬렉션 일시 중지를 갖고 고정된 상수 메모리 오버헤드를 발생시키며 응용 프로그램 코드와의 동기화나 장벽이 필요하지 않다. 이를 통해 응용 프로그램이 사용 가능한 속도로 얼마나 자주 응답하는지를 의미하는 성능을 지원하는 소프트웨어 스택을 만들기 위한 비전을 제시한다.

## 🎯 주요 포인트


- 어플리케이션의 성능은 메모리 및 시간 사용량이 적을수록 더 우수하다.

- 어플리케이션의 우수한 성능은 주로 95번째 및 99번째 백분위수 tail-latencies에 초점을 맞춘다.

- Bosque 프로그래밍 언어 및 런타임을 위한 새로운 가비지 컬렉터 디자인, Catalpa 컬렉터를 제안한다.


---

*Generated on 2025-09-18 17:23:17*