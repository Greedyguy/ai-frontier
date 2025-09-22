
# TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding

**Korean Title:** TableDART: 표 이해를 위한 동적 적응형 다중 모달 라우팅

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Adaptive Routing

## 🔗 유사한 논문
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.4% similar)
- [[(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (80.8% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.8% similar)
- [[Process-Supervised_Reinforcement_Learning_for_Interactive_Multimodal_Tool-Use_Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (80.5% similar)
- [[DRDT3 Diffusion-Refined Decision Test-Time Training Model]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14671v1 Announce Type: cross 
Abstract: Modeling semantic and structural information from tabular data remains a core challenge for effective table understanding. Existing Table-as-Text approaches flatten tables for large language models (LLMs), but lose crucial structural cues, while Table-as-Image methods preserve structure yet struggle with fine-grained semantics. Recent Table-as-Multimodality strategies attempt to combine textual and visual views, but they (1) statically process both modalities for every query-table pair within a large multimodal LLMs (MLLMs), inevitably introducing redundancy and even conflicts, and (2) depend on costly fine-tuning of MLLMs. In light of this, we propose TableDART, a training-efficient framework that integrates multimodal views by reusing pretrained single-modality models. TableDART introduces a lightweight 2.59M-parameter MLP gating network that dynamically selects the optimal path (either Text-only, Image-only, or Fusion) for each table-query pair, effectively reducing redundancy and conflicts from both modalities. In addition, we propose a novel agent to mediate cross-modal knowledge integration by analyzing outputs from text- and image-based models, either selecting the best result or synthesizing a new answer through reasoning. This design avoids the prohibitive costs of full MLLM fine-tuning. Extensive experiments on seven benchmarks show that TableDART establishes new state-of-the-art performance among open-source models, surpassing the strongest baseline by an average of 4.02%. The code is available at: https://anonymous.4open.science/r/TableDART-C52B

## 🔍 Abstract (한글 번역)

arXiv:2509.14671v1 발표 유형: 교차  
초록: 표 데이터를 이해하는 데 있어 의미적 및 구조적 정보를 모델링하는 것은 여전히 핵심 과제입니다. 기존의 텍스트로서의 표 접근 방식은 대형 언어 모델(LLM)을 위해 표를 평탄화하지만 중요한 구조적 단서를 잃어버리며, 이미지로서의 표 방법은 구조를 보존하지만 세밀한 의미를 처리하는 데 어려움을 겪습니다. 최근의 멀티모달리티로서의 표 전략은 텍스트 및 시각적 관점을 결합하려고 시도하지만, (1) 대형 멀티모달 LLM(MLLM) 내에서 모든 쿼리-표 쌍에 대해 두 가지 모달리티를 정적으로 처리하여 불가피하게 중복 및 충돌을 초래하고, (2) MLLM의 비용이 많이 드는 미세 조정에 의존합니다. 이를 고려하여, 우리는 사전 훈련된 단일 모달리티 모델을 재사용하여 멀티모달 관점을 통합하는 훈련 효율적인 프레임워크인 TableDART를 제안합니다. TableDART는 각 표-쿼리 쌍에 대해 최적의 경로(텍스트 전용, 이미지 전용 또는 융합)를 동적으로 선택하는 경량의 2.59M-파라미터 MLP 게이팅 네트워크를 도입하여 두 모달리티의 중복 및 충돌을 효과적으로 줄입니다. 또한, 우리는 텍스트 및 이미지 기반 모델의 출력을 분석하여 최상의 결과를 선택하거나 추론을 통해 새로운 답변을 합성함으로써 교차 모달 지식 통합을 중재하는 새로운 에이전트를 제안합니다. 이 설계는 전체 MLLM 미세 조정의 과도한 비용을 피합니다. 일곱 가지 벤치마크에 대한 광범위한 실험은 TableDART가 오픈 소스 모델 중 새로운 최첨단 성능을 확립하며, 가장 강력한 기준선을 평균 4.02% 초과함을 보여줍니다. 코드는 다음에서 확인할 수 있습니다: https://anonymous.4open.science/r/TableDART-C52B

## 📝 요약

TableDART는 테이블 데이터의 의미와 구조 정보를 효과적으로 모델링하기 위한 새로운 프레임워크로, 기존의 Table-as-Text와 Table-as-Image 접근법의 한계를 극복합니다. 이 프레임워크는 사전 학습된 단일 모달리티 모델을 재사용하여 멀티모달 뷰를 통합하며, 2.59M 파라미터의 MLP 게이팅 네트워크를 통해 각 테이블-쿼리 쌍에 대해 최적의 경로를 동적으로 선택합니다. 또한, 텍스트 및 이미지 기반 모델의 출력을 분석하여 최적의 결과를 선택하거나 새로운 답변을 합성하는 에이전트를 제안합니다. 이 접근법은 MLLM의 비용이 많이 드는 미세 조정을 피하면서도, 7개의 벤치마크 실험에서 평균 4.02%의 성능 향상을 달성하며 새로운 최첨단 성능을 기록했습니다.

## 🎯 주요 포인트

- 1. TableDART는 사전 학습된 단일 모달리티 모델을 재사용하여 멀티모달 뷰를 통합하는 효율적인 프레임워크를 제안합니다.

- 2. 2.59M 파라미터의 경량 MLP 게이팅 네트워크를 도입하여 각 테이블-쿼리 쌍에 대해 최적의 경로를 동적으로 선택합니다.

- 3. 텍스트 및 이미지 기반 모델의 출력을 분석하여 최상의 결과를 선택하거나 새로운 답변을 합성하는 교차 모달 지식 통합 에이전트를 제안합니다.

- 4. TableDART는 오픈 소스 모델 중 새로운 최첨단 성능을 달성하며, 가장 강력한 기준선보다 평균 4.02% 더 높은 성능을 보입니다.

---

*Generated on 2025-09-19 14:59:43*