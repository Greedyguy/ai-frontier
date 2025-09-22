# AmpleHate: Amplifying the Attention for Versatile Implicit Hate Detection

**Korean Title:** AmpleHate: 다양한 암묵적 혐오 감지를 위한 주의 증폭

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Implicit Hate Detection

## 🔗 유사한 논문
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (81.5% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (80.4% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (80.0% similar)
- [[2025-09-22/KatFishNet_ Detecting LLM-Generated Korean Text through Linguistic Feature Analysis_20250922|KatFishNet Detecting LLM-Generated Korean Text through Linguistic Feature Analysis]] (79.6% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19528v3 Announce Type: replace-cross 
Abstract: Implicit hate speech detection is challenging due to its subtlety and reliance on contextual interpretation rather than explicit offensive words. Current approaches rely on contrastive learning, which are shown to be effective on distinguishing hate and non-hate sentences. Humans, however, detect implicit hate speech by first identifying specific targets within the text and subsequently interpreting how these target relate to their surrounding context. Motivated by this reasoning process, we propose AmpleHate, a novel approach designed to mirror human inference for implicit hate detection. AmpleHate identifies explicit target using a pretrained Named Entity Recognition model and capture implicit target information via [CLS] tokens. It computes attention-based relationships between explicit, implicit targets and sentence context and then, directly injects these relational vectors into the final sentence representation. This amplifies the critical signals of target-context relations for determining implicit hate. Experiments demonstrate that AmpleHate achieves state-of-the-art performance, outperforming contrastive learning baselines by an average of 82.14% and achieve faster convergence. Qualitative analyses further reveal that attention patterns produced by AmpleHate closely align with human judgement, underscoring its interpretability and robustness. Our code is publicly available at: https://github.com/leeyejin1231/AmpleHate.

## 🔍 Abstract (한글 번역)

arXiv:2505.19528v3 발표 유형: 교차 교체  
초록: 암시적 혐오 발언 탐지는 그 미묘함과 명시적인 공격적 단어보다는 맥락적 해석에 의존하기 때문에 어려운 과제입니다. 현재의 접근 방식은 대조 학습에 의존하며, 이는 혐오 문장과 비혐오 문장을 구별하는 데 효과적인 것으로 나타났습니다. 그러나 인간은 먼저 텍스트 내 특정 대상을 식별한 후 이러한 대상이 주변 맥락과 어떻게 관련되는지를 해석하여 암시적 혐오 발언을 탐지합니다. 이러한 추론 과정을 바탕으로, 우리는 암시적 혐오 탐지를 위한 인간의 추론을 모방하도록 설계된 새로운 접근 방식인 AmpleHate를 제안합니다. AmpleHate는 사전 학습된 명명된 개체 인식 모델을 사용하여 명시적 대상을 식별하고 [CLS] 토큰을 통해 암시적 대상 정보를 포착합니다. 그런 다음 명시적, 암시적 대상과 문장 맥락 간의 주의 기반 관계를 계산하고, 이러한 관계 벡터를 최종 문장 표현에 직접 주입합니다. 이는 암시적 혐오를 결정하기 위한 대상-맥락 관계의 중요한 신호를 증폭시킵니다. 실험 결과 AmpleHate는 최첨단 성능을 달성하며, 대조 학습 기준을 평균 82.14% 초과하여 더 빠른 수렴을 이룹니다. 질적 분석은 또한 AmpleHate가 생성한 주의 패턴이 인간의 판단과 밀접하게 일치함을 보여주어 그 해석 가능성과 강건성을 강조합니다. 우리의 코드는 다음에서 공개적으로 사용할 수 있습니다: https://github.com/leeyejin1231/AmpleHate.

## 📝 요약

이 논문은 암묵적 혐오 발언 탐지를 위한 새로운 접근법인 AmpleHate를 제안합니다. 기존의 대조 학습 방법은 혐오와 비혐오 문장을 구분하는 데 효과적이지만, AmpleHate는 인간의 추론 과정을 모방하여 명시적 및 암묵적 대상을 식별하고 문맥과의 관계를 강화합니다. 이를 위해 사전 학습된 개체명 인식 모델을 사용하고, [CLS] 토큰을 통해 암묵적 대상 정보를 캡처합니다. 실험 결과, AmpleHate는 기존 방법보다 평균 82.14% 더 높은 성능을 보이며, 수렴 속도도 빠릅니다. 또한, 주의 패턴이 인간의 판단과 유사하게 나타나 해석 가능성과 견고성을 강조합니다.

## 🎯 주요 포인트

- 1. 암묵적 혐오 발언 탐지는 명시적인 공격적 언어 대신 문맥적 해석에 의존하기 때문에 도전적이다.

- 2. AmpleHate는 인간의 추론 과정을 모방하여 명시적 및 암묵적 대상을 식별하고, 이들 간의 관계를 문장 표현에 직접 주입하여 암묵적 혐오를 탐지한다.

- 3. AmpleHate는 명명된 개체 인식 모델을 사용하여 명시적 대상을 식별하고, [CLS] 토큰을 통해 암묵적 대상 정보를 포착한다.

- 4. 실험 결과, AmpleHate는 기존의 대조 학습 기반 모델보다 평균 82.14% 더 나은 성능을 보이며, 빠른 수렴을 달성한다.

- 5. AmpleHate의 주의 패턴은 인간의 판단과 밀접하게 일치하여 해석 가능성과 견고성을 강조한다.

---

*Generated on 2025-09-22 14:51:13*