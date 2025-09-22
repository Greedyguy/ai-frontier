# ORIC: Benchmarking Object Recognition in Incongruous Context for Large Vision-Language Models

**Korean Title:** ORIC: 대규모 비전-언어 모델을 위한 부조화 맥락에서의 객체 인식 벤치마킹

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Contextual Incongruity

## 🔗 유사한 논문
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (88.7% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1 Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (82.5% similar)
- [[2025-09-18/The Art of Saying Maybe_ A Conformal Lens for Uncertainty Benchmarking in VLMs_20250918|The Art of Saying Maybe A Conformal Lens for Uncertainty Benchmarking in VLMs]] (81.5% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (81.1% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (80.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15695v1 Announce Type: cross 
Abstract: Large Vision-Language Models (LVLMs) have made significant strides in image caption, visual question answering, and robotics by integrating visual and textual information. However, they remain prone to errors in incongruous contexts, where objects appear unexpectedly or are absent when contextually expected. This leads to two key recognition failures: object misidentification and hallucination. To systematically examine this issue, we introduce the Object Recognition in Incongruous Context Benchmark (ORIC), a novel benchmark that evaluates LVLMs in scenarios where object-context relationships deviate from expectations. ORIC employs two key strategies: (1) LLM-guided sampling, which identifies objects that are present but contextually incongruous, and (2) CLIP-guided sampling, which detects plausible yet nonexistent objects that are likely to be hallucinated, thereby creating an incongruous context. Evaluating 18 LVLMs and two open-vocabulary detection models, our results reveal significant recognition gaps, underscoring the challenges posed by contextual incongruity. This work provides critical insights into LVLMs' limitations and encourages further research on context-aware object recognition.

## 🔍 Abstract (한글 번역)

arXiv:2509.15695v1 발표 유형: 교차  
초록: 대형 비전-언어 모델(LVLMs)은 시각적 및 텍스트 정보를 통합하여 이미지 캡션, 시각적 질문 응답 및 로봇 공학 분야에서 상당한 발전을 이루었습니다. 그러나 이러한 모델은 예상치 못한 상황에서 객체가 나타나거나 맥락상 예상되는 객체가 없는 경우 오류를 범하기 쉽습니다. 이는 두 가지 주요 인식 실패로 이어집니다: 객체 오인식과 환각. 이 문제를 체계적으로 조사하기 위해, 우리는 객체-맥락 관계가 기대에서 벗어나는 시나리오에서 LVLMs를 평가하는 새로운 벤치마크인 불일치 맥락에서의 객체 인식 벤치마크(ORIC)를 소개합니다. ORIC는 두 가지 주요 전략을 사용합니다: (1) LLM-유도 샘플링, 이는 존재하지만 맥락상 불일치한 객체를 식별하고, (2) CLIP-유도 샘플링, 이는 환각될 가능성이 높은 그럴듯하지만 존재하지 않는 객체를 감지하여 불일치한 맥락을 생성합니다. 18개의 LVLMs와 두 개의 개방형 어휘 탐지 모델을 평가한 결과, 맥락 불일치로 인한 인식 격차가 상당함을 밝혀내며, 맥락적 불일치가 제기하는 도전을 강조합니다. 이 연구는 LVLMs의 한계에 대한 중요한 통찰을 제공하며, 맥락 인식 객체 인식에 대한 추가 연구를 장려합니다.

## 📝 요약

대규모 비전-언어 모델(LVLMs)은 이미지 캡션, 시각적 질문 응답, 로봇 공학에서 큰 발전을 이루었지만, 예상치 못한 맥락에서 객체를 잘못 인식하거나 환각하는 오류가 발생합니다. 이를 해결하기 위해, 우리는 객체-맥락 관계가 예상과 다른 시나리오를 평가하는 새로운 벤치마크인 ORIC(Object Recognition in Incongruous Context Benchmark)을 도입했습니다. ORIC는 LLM과 CLIP 가이드 샘플링을 통해 맥락적으로 부적절하거나 존재하지 않는 객체를 식별합니다. 18개의 LVLM과 두 개의 개방형 어휘 탐지 모델을 평가한 결과, 맥락적 부조화로 인한 인식 격차가 크게 나타났습니다. 이 연구는 LVLM의 한계를 밝히고 맥락 인식 객체 인식에 대한 추가 연구를 촉진합니다.

## 🎯 주요 포인트

- 1. 대형 비전-언어 모델(LVLMs)은 이미지 캡션, 시각적 질문 응답, 로봇 공학에서 시각적 및 텍스트 정보를 통합하여 발전을 이루었지만, 부적절한 문맥에서 오류를 범하기 쉽습니다.

- 2. LVLMs의 주요 인식 실패는 객체 오인식과 환각 현상으로, 기대와 다른 객체-문맥 관계에서 발생합니다.

- 3. 새로운 벤치마크인 ORIC는 객체-문맥 관계가 기대와 다른 시나리오에서 LVLMs를 평가하기 위해 도입되었습니다.

- 4. ORIC는 LLM-가이드 샘플링과 CLIP-가이드 샘플링을 사용하여 문맥적으로 부적절하거나 존재하지 않는 객체를 식별합니다.

- 5. 18개의 LVLMs와 두 개의 오픈 보캐뷸러리 감지 모델을 평가한 결과, 문맥적 부적절성으로 인한 인식 격차가 크게 드러났습니다.

---

*Generated on 2025-09-22 15:41:24*