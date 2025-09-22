
# Soft Graph Transformer for MIMO Detection

**Korean Title:** MIMO 감지를 위한 소프트 그래프 트랜스포머

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Structured Message Passing

## 🔗 유사한 논문
- [[GraphTorque_Torque-Driven_Rewiring_Graph_Neural_Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (77.0% similar)
- [[Multimodal Hate Detection Using Dual-Stream Graph Neural Networks]] (76.0% similar)
- [[CSMoE_An_Efficient_Remote_Sensing_Foundation_Model_with_Soft_Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (76.0% similar)
- [[BERTector_An_Intrusion_Detection_Framework_Constructed_via_Joint-dataset_Learning_Based_on_Language_Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (75.5% similar)
- [[TFLAGTowards_Practical_APT_Detection_via_Deviation-Aware_Learning_on_Temporal_Provenance_Graph_20250918|TFLAG:Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph]] (75.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12694v2 Announce Type: replace 
Abstract: We propose the Soft Graph Transformer (SGT), a soft-input-soft-output neural architecture designed for MIMO detection. While Maximum Likelihood (ML) detection achieves optimal accuracy, its exponential complexity makes it infeasible in large systems, and conventional message-passing algorithms rely on asymptotic assumptions that often fail in finite dimensions. Recent Transformer-based detectors show strong performance but typically overlook the MIMO factor graph structure and cannot exploit prior soft information. SGT addresses these limitations by combining self-attention, which encodes contextual dependencies within symbol and constraint subgraphs, with graph-aware cross-attention, which performs structured message passing across subgraphs. Its soft-input interface allows the integration of auxiliary priors, producing effective soft outputs while maintaining computational efficiency. Experiments demonstrate that SGT achieves near-ML performance and offers a flexible and interpretable framework for receiver systems that leverage soft priors.

## 🔍 Abstract (한글 번역)

arXiv:2509.12694v2 발표 유형: 대체
요약: 우리는 MIMO 감지를 위해 설계된 소프트 입력-소프트 출력 신경 구조 인 Soft Graph Transformer (SGT)를 제안합니다. 최대 우도 (ML) 감지는 최적의 정확도를 달성하지만 지수적 복잡성으로 인해 대규모 시스템에서 불가능하며, 전통적인 메시지 전달 알고리즘은 종족적 가정에 의존하여 종족적 가정이 종종 유한 차원에서 실패합니다. 최근의 Transformer 기반 감지기는 강력한 성능을 보여주지만 일반적으로 MIMO 팩터 그래프 구조를 간과하고 이전의 소프트 정보를 활용할 수 없습니다. SGT는 심볼 및 제약 부분 그래프 내에서 문맥 의존성을 인코딩하는 자기 주의(self-attention)와 부분 그래프 간에 구조화된 메시지 전달을 수행하는 그래프 인식 교차 주의(cross-attention)를 결합하여 이러한 제한 사항을 해결합니다. 그의 소프트 입력 인터페이스는 보조 사전을 통합하여 효과적인 소프트 출력을 생성하면서 계산 효율성을 유지합니다. 실험 결과는 SGT가 거의 ML 성능을 달성하고 소프트 사전을 활용하는 수신기 시스템에 대해 유연하고 해석 가능한 프레임워크를 제공한다는 것을 보여줍니다.

## 📝 요약

본 연구에서는 MIMO 검출을 위해 설계된 소프트 입력-소프트 출력 신경 구조 인 Soft Graph Transformer (SGT)를 제안합니다. 최대 우도 (ML) 검출은 최적의 정확도를 달성하지만 지수적인 복잡성으로 인해 대규모 시스템에서 실행하기 어렵고, 전통적인 메시지 전달 알고리즘은 종종 유한 차원에서 실패합니다. 최근 Transformer 기반 검출기는 강력한 성능을 보이지만 일반적으로 MIMO 요인 그래프 구조를 간과하고 소프트 정보를 활용할 수 없습니다. SGT는 심볼 및 제약 부분 그래프 내에서 문맥 의존성을 인코딩하는 self-attention과 부분 그래프 간에 구조화된 메시지 전달을 수행하는 그래프 인식 cross-attention을 결합하여 이러한 한계를 해결합니다. 실험 결과, SGT는 거의 ML 성능을 달성하며 소프트 사전을 활용하는 수신기 시스템에 대한 유연하고 해석 가능한 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. Soft Graph Transformer (SGT)는 MIMO 감지를 위해 설계된 소프트 입력-소프트 출력 신경 구조이다.

- 2. SGT는 자기 주의(self-attention)와 그래프 인식 교차 주의(graph-aware cross-attention)를 결합하여 제한 서브그래프 간에 구조화된 메시지 전달을 수행한다.

- 3. SGT는 부가적인 사전 정보를 통합하여 효과적인 소프트 출력을 생성하면서 계산 효율성을 유지한다.

---

*Generated on 2025-09-18 16:48:20*