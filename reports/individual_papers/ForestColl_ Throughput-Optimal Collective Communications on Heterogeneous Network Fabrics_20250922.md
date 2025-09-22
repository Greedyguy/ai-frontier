# ForestColl: Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics

**Korean Title:** ForestColl: 이기종 네트워크 패브릭에서 처리량 최적화를 위한 집합적 통신

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Spanning Tree Communication|Spanning Tree Communication]] [[keywords/specific/Throughput-Optimal Schedules|Throughput-Optimal Schedules]] [[keywords/broad/Collective Communications|Collective Communications]] [[keywords/broad/Network Fabrics|Network Fabrics]] [[keywords/unique/ForestColl|ForestColl]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (78.8% similar) [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (78.8% similar) [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Heterogeneous Network Fabrics
**🔗 Specific Connectable**: Throughput Optimal Schedules
**🔬 Broad Technical**: Deep Neural Networks, Collective Communications
**⭐ Unique Technical**: ForestColl
## 🔗 유사한 논문
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (78.8% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (78.8% similar)
- [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (78.7% similar)
- [[2025-09-18/Catalpa_ GC for a Low-Variance Software Stack_20250918|Catalpa GC for a Low-Variance Software Stack]] (78.5% similar)
- [[2025-09-22/DebFlow_ Automating Agent Creation via Agent Debate_20250922|DebFlow Automating Agent Creation via Agent Debate]] (78.4% similar)


**ArXiv ID**: [2402.06787](https://arxiv.org/abs/2402.06787)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2402.06787.pdf)


**ArXiv ID**: [2402.06787](https://arxiv.org/abs/2402.06787)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2402.06787.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Spanning Trees for Communication
**🔗 Specific Connectable**: Throughput-Optimal Schedules
**⭐ Unique Technical**: ForestColl
**🔬 Broad Technical**: Collective Communications, Network Fabrics

## 🏷️ 추출된 키워드



`Collective Communications` • 

`Network Fabrics` • 

`Throughput Optimal Schedules` • 

`ForestColl` • 

`Spanning Tree Communication`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2402.06787v4 Announce Type: replace-cross 
Abstract: As modern DNN models grow ever larger, collective communications between the accelerators (allreduce, etc.) emerge as a significant performance bottleneck. Designing efficient communication schedules is challenging, given today's heterogeneous and diverse network fabrics. We present ForestColl, a tool that generates throughput-optimal schedules for any network topology. ForestColl constructs broadcast/aggregation spanning trees as the communication schedule, achieving theoretical optimality. Its schedule generation runs in polynomial time and is highly scalable. ForestColl supports any network fabric, including both switching fabrics and direct accelerator connections. We evaluated ForestColl on AMD MI250 and NVIDIA DGX A100 & H100 clusters. ForestColl showed significant improvements over the vendors' own optimized communication libraries across various settings and in LLM training. ForestColl also outperformed other state-of-the-art schedule generation techniques with both more efficient generated schedules and substantially faster generation speed.

## 🔍 Abstract (한글 번역)

arXiv:2402.06787v4 발표 유형: 교차 교체  
초록: 현대의 DNN 모델이 점점 더 커짐에 따라 가속기 간의 집단 통신(예: allreduce 등)이 중요한 성능 병목 현상으로 부각되고 있습니다. 오늘날의 이질적이고 다양한 네트워크 패브릭을 고려할 때 효율적인 통신 스케줄을 설계하는 것은 도전적입니다. 우리는 ForestColl을 소개합니다. 이는 어떤 네트워크 토폴로지에서도 처리량 최적의 스케줄을 생성하는 도구입니다. ForestColl은 브로드캐스트/집계 스패닝 트리를 통신 스케줄로 구성하여 이론적 최적성을 달성합니다. 스케줄 생성은 다항 시간 내에 실행되며 매우 확장성이 뛰어납니다. ForestColl은 스위칭 패브릭과 직접 가속기 연결을 포함한 모든 네트워크 패브릭을 지원합니다. 우리는 AMD MI250 및 NVIDIA DGX A100 & H100 클러스터에서 ForestColl을 평가했습니다. ForestColl은 다양한 설정과 LLM 훈련에서 벤더의 자체 최적화된 통신 라이브러리에 비해 상당한 개선을 보여주었습니다. ForestColl은 또한 더 효율적인 생성 스케줄과 훨씬 더 빠른 생성 속도로 다른 최첨단 스케줄 생성 기술을 능가했습니다.

## 📝 요약

현대의 대규모 DNN 모델에서 가속기 간의 집단 통신은 성능 병목 현상이 됩니다. 이를 해결하기 위해 다양한 네트워크 구조에 최적화된 통신 스케줄을 생성하는 ForestColl을 제안합니다. ForestColl은 브로드캐스트/집계 스패닝 트리를 사용하여 이론적으로 최적의 통신 스케줄을 생성하며, 다항 시간 내에 실행 가능하고 확장성이 뛰어납니다. AMD MI250 및 NVIDIA DGX A100 & H100 클러스터에서 평가한 결과, ForestColl은 벤더의 최적화된 통신 라이브러리보다 뛰어난 성능을 보였으며, LLM 훈련에서도 우수한 성능을 입증했습니다. 또한, 다른 최신 스케줄 생성 기법보다 더 효율적이고 빠르게 스케줄을 생성했습니다.

## 🎯 주요 포인트


- 1. ForestColl은 네트워크 토폴로지에 최적화된 통신 스케줄을 생성하는 도구로, 이론적 최적 성능을 달성합니다.

- 2. 이 도구는 브로드캐스트/집계 스패닝 트리를 사용하여 통신 스케줄을 구성하며, 다항 시간 내에 스케줄을 생성할 수 있어 높은 확장성을 자랑합니다.

- 3. ForestColl은 스위칭 패브릭 및 직접 가속기 연결을 포함한 모든 네트워크 패브릭을 지원합니다.

- 4. AMD MI250 및 NVIDIA DGX A100 & H100 클러스터에서 평가한 결과, ForestColl은 벤더의 최적화된 통신 라이브러리보다 뛰어난 성능을 보였습니다.

- 5. ForestColl은 최신 스케줄 생성 기술보다 더 효율적인 스케줄을 생성하며, 생성 속도 또한 크게 향상되었습니다.


---

*Generated on 2025-09-22 16:05:27*