
# MARIC: Multi-Agent Reasoning for Image Classification

**Korean Title:** MARIC: 이미지 분류를 위한 다중 에이전트 추론

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent Reasoning

## 🔗 유사한 논문
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.0% similar)
- [[Uni-cot Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (81.9% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.6% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (81.0% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14860v1 Announce Type: cross 
Abstract: Image classification has traditionally relied on parameter-intensive model training, requiring large-scale annotated datasets and extensive fine tuning to achieve competitive performance. While recent vision language models (VLMs) alleviate some of these constraints, they remain limited by their reliance on single pass representations, often failing to capture complementary aspects of visual content. In this paper, we introduce Multi Agent based Reasoning for Image Classification (MARIC), a multi agent framework that reformulates image classification as a collaborative reasoning process. MARIC first utilizes an Outliner Agent to analyze the global theme of the image and generate targeted prompts. Based on these prompts, three Aspect Agents extract fine grained descriptions along distinct visual dimensions. Finally, a Reasoning Agent synthesizes these complementary outputs through integrated reflection step, producing a unified representation for classification. By explicitly decomposing the task into multiple perspectives and encouraging reflective synthesis, MARIC mitigates the shortcomings of both parameter-heavy training and monolithic VLM reasoning. Experiments on 4 diverse image classification benchmark datasets demonstrate that MARIC significantly outperforms baselines, highlighting the effectiveness of multi-agent visual reasoning for robust and interpretable image classification.

## 🔍 Abstract (한글 번역)

arXiv:2509.14860v1 발표 유형: 교차  
초록: 이미지 분류는 전통적으로 대규모 주석 데이터셋과 광범위한 미세 조정을 필요로 하는 매개변수 집약적인 모델 훈련에 의존해 왔으며, 경쟁력 있는 성능을 달성하기 위해 많은 노력이 필요했습니다. 최근의 비전 언어 모델(VLM)은 이러한 제약을 일부 완화하지만, 단일 패스 표현에 의존하여 시각적 콘텐츠의 보완적 측면을 포착하지 못하는 경우가 많습니다. 본 논문에서는 이미지 분류를 협력적 추론 과정으로 재구성하는 다중 에이전트 프레임워크인 이미지 분류를 위한 다중 에이전트 기반 추론(MARIC)을 소개합니다. MARIC는 먼저 아웃라이너 에이전트를 사용하여 이미지의 전반적인 테마를 분석하고 목표 지향적인 프롬프트를 생성합니다. 이러한 프롬프트를 기반으로 세 가지 측면 에이전트가 서로 다른 시각적 차원에 따라 세밀한 설명을 추출합니다. 마지막으로, 추론 에이전트는 통합 반영 단계를 통해 이러한 보완적 출력을 종합하여 분류를 위한 통합된 표현을 생성합니다. 작업을 여러 관점으로 명시적으로 분해하고 반영적 종합을 장려함으로써, MARIC는 매개변수 집약적인 훈련과 단일체 VLM 추론의 단점을 완화합니다. 4개의 다양한 이미지 분류 벤치마크 데이터셋에 대한 실험 결과, MARIC는 기준선을 크게 능가하여 견고하고 해석 가능한 이미지 분류를 위한 다중 에이전트 시각적 추론의 효과를 강조합니다.

## 📝 요약

전통적인 이미지 분류는 대규모 주석 데이터와 세밀한 조정이 필요한 모델 훈련에 의존해 왔습니다. 최근의 비전 언어 모델(VLM)은 이러한 제약을 일부 완화했지만, 단일 패스 표현에 의존하여 시각적 콘텐츠의 보완적 측면을 포착하지 못하는 한계가 있습니다. 본 논문에서는 이미지 분류를 협력적 추론 과정으로 재구성하는 다중 에이전트 프레임워크인 MARIC를 소개합니다. MARIC는 먼저 아웃라이너 에이전트를 사용하여 이미지의 전반적인 주제를 분석하고 목표 지향적 프롬프트를 생성합니다. 그런 다음 세 가지 측면 에이전트가 서로 다른 시각적 차원에서 세부적인 설명을 추출합니다. 마지막으로, 추론 에이전트가 이러한 보완적 출력을 통합하여 통합된 표현을 생성합니다. MARIC는 다중 관점을 통해 작업을 명시적으로 분해하고 반영적 통합을 장려하여 매개변수 집약적 훈련과 단일 VLM 추론의 단점을 완화합니다. 4개의 다양한 이미지 분류 벤치마크 데이터셋 실험에서 MARIC는 기존 모델을 능가하여 견고하고 해석 가능한 이미지 분류를 위한 다중 에이전트 시각적 추론의 효과를 입증합니다.

## 🎯 주요 포인트

- 1. 전통적인 이미지 분류는 대규모 주석 데이터셋과 세밀한 튜닝이 필요한 매개변수 집약적 모델 훈련에 의존해왔다.

- 2. Multi Agent based Reasoning for Image Classification (MARIC)은 이미지 분류를 협력적 추론 과정으로 재구성하는 다중 에이전트 프레임워크를 도입한다.

- 3. MARIC은 Outliner Agent를 통해 이미지의 전반적인 주제를 분석하고, 세 가지 Aspect Agents가 각기 다른 시각적 차원에서 세부 설명을 추출한다.

- 4. Reasoning Agent는 통합 반영 단계를 통해 이러한 보완적 출력을 종합하여 분류를 위한 통합 표현을 생성한다.

- 5. MARIC은 다양한 이미지 분류 벤치마크 데이터셋 실험에서 기존 방법보다 뛰어난 성능을 보여주며, 견고하고 해석 가능한 이미지 분류를 위한 다중 에이전트 시각적 추론의 효과를 강조한다.

---

*Generated on 2025-09-19 15:01:28*