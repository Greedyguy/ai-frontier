
# Generalizable Geometric Image Caption Synthesis

**Korean Title:** 일반화 가능한 기하학적 이미지 캡션 합성

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Task Generalization in Geometry Problem Solving

## 🔗 유사한 논문
- [[THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (82.5% similar)
- [[GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (82.3% similar)
- [[Video-Language Critic Transferable Reward Functions for Language-Conditioned Robotics]] (81.9% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.7% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15217v1 Announce Type: new 
Abstract: Multimodal large language models have various practical applications that demand strong reasoning abilities. Despite recent advancements, these models still struggle to solve complex geometric problems. A key challenge stems from the lack of high-quality image-text pair datasets for understanding geometric images. Furthermore, most template-based data synthesis pipelines typically fail to generalize to questions beyond their predefined templates. In this paper, we bridge this gap by introducing a complementary process of Reinforcement Learning with Verifiable Rewards (RLVR) into the data generation pipeline. By adopting RLVR to refine captions for geometric images synthesized from 50 basic geometric relations and using reward signals derived from mathematical problem-solving tasks, our pipeline successfully captures the key features of geometry problem-solving. This enables better task generalization and yields non-trivial improvements. Furthermore, even in out-of-distribution scenarios, the generated dataset enhances the general reasoning capabilities of multimodal large language models, yielding accuracy improvements of $2.8\%\text{-}4.8\%$ in statistics, arithmetic, algebraic, and numerical tasks with non-geometric input images of MathVista and MathVerse, along with $2.4\%\text{-}3.9\%$ improvements in Art, Design, Tech, and Engineering tasks in MMMU.

## 🔍 Abstract (한글 번역)

arXiv:2509.15217v1 발표 유형: 신규  
초록: 다중 모달 대형 언어 모델은 강력한 추론 능력을 요구하는 다양한 실용적인 응용 프로그램을 가지고 있습니다. 최근의 발전에도 불구하고, 이러한 모델은 여전히 복잡한 기하학적 문제를 해결하는 데 어려움을 겪고 있습니다. 주요 도전 과제는 기하학적 이미지를 이해하기 위한 고품질 이미지-텍스트 쌍 데이터셋의 부족에서 비롯됩니다. 게다가, 대부분의 템플릿 기반 데이터 합성 파이프라인은 미리 정의된 템플릿을 넘어서는 질문에 일반화하는 데 실패하는 경우가 많습니다. 이 논문에서는 검증 가능한 보상(Reinforcement Learning with Verifiable Rewards, RLVR)을 데이터 생성 파이프라인에 도입하여 이 격차를 해소합니다. 50개의 기본 기하학적 관계에서 합성된 기하학적 이미지에 대한 캡션을 개선하기 위해 RLVR을 채택하고 수학 문제 해결 작업에서 파생된 보상 신호를 사용함으로써, 우리의 파이프라인은 기하학 문제 해결의 핵심 특징을 성공적으로 포착합니다. 이는 더 나은 작업 일반화를 가능하게 하고 비트리비얼한 개선을 제공합니다. 또한, 분포 외 시나리오에서도 생성된 데이터셋은 다중 모달 대형 언어 모델의 일반 추론 능력을 향상시켜 MathVista와 MathVerse의 비기하학적 입력 이미지에서 통계, 산술, 대수, 수치 작업에서 $2.8\%\text{-}4.8\%$의 정확도 향상을, MMMU의 예술, 디자인, 기술, 공학 작업에서 $2.4\%\text{-}3.9\%$의 향상을 제공합니다.

## 📝 요약

이 논문은 복잡한 기하학적 문제 해결 능력을 향상시키기 위해 다중모달 대형 언어 모델에 Reinforcement Learning with Verifiable Rewards (RLVR) 기법을 도입한 연구를 소개합니다. 기존의 데이터셋이 기하학적 이미지 이해에 한계가 있어, RLVR을 활용하여 50개의 기본 기하학적 관계에서 생성된 이미지의 캡션을 개선하고, 수학적 문제 해결 과제에서 파생된 보상 신호를 사용하여 데이터 생성 파이프라인을 강화했습니다. 이 방법은 기하학 문제 해결의 핵심 특징을 포착하여 더 나은 과제 일반화를 가능하게 하고, 통계, 산술, 대수 및 수치 작업에서 2.8%에서 4.8%의 정확도 향상을 달성했습니다. 또한, Art, Design, Tech, Engineering 작업에서도 2.4%에서 3.9%의 개선을 보여주었습니다.

## 🎯 주요 포인트

- 1. 다중 모달 대형 언어 모델은 복잡한 기하학적 문제 해결에 어려움을 겪고 있습니다.

- 2. 고품질의 이미지-텍스트 쌍 데이터셋 부족이 기하학적 이미지 이해의 주요 도전 과제로 작용합니다.

- 3. 본 연구는 강화 학습과 검증 가능한 보상(RLVR)을 데이터 생성 파이프라인에 도입하여 이 문제를 해결합니다.

- 4. RLVR을 통해 생성된 데이터셋은 기하학 문제 해결의 주요 특징을 포착하여 모델의 일반화 능력을 향상시킵니다.

- 5. 생성된 데이터셋은 다양한 비기하학적 입력 이미지와 과제에서 모델의 정확도를 2.8%에서 4.8%까지 개선합니다.

---

*Generated on 2025-09-19 14:50:02*