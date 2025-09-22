# Creative Preference Optimization

**Korean Title:** 창의적 선호 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Creativity Augmentation

## 🔗 유사한 논문
- [[2025-09-18/Evolving Language Models without Labels_ Majority Drives Selection, Novelty Promotes Variation_20250918|Evolving Language Models without Labels Majority Drives Selection, Novelty Promotes Variation]] (83.3% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.2% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (83.0% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.8% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14442v2 Announce Type: replace-cross 
Abstract: While Large Language Models (LLMs) have demonstrated impressive performance across natural language generation tasks, their ability to generate truly creative content-characterized by novelty, diversity, surprise, and quality-remains limited. Existing methods for enhancing LLM creativity often focus narrowly on diversity or specific tasks, failing to address creativity's multifaceted nature in a generalizable way. In this work, we propose Creative Preference Optimization (CrPO), a novel alignment method that injects signals from multiple creativity dimensions into the preference optimization objective in a modular fashion. We train and evaluate creativity-augmented versions of several models using CrPO and MuCE, a new large-scale human preference dataset spanning over 200,000 human-generated responses and ratings from more than 30 psychological creativity assessments. Our models outperform strong baselines, including GPT-4o, on both automated and human evaluations, producing more novel, diverse, and surprising generations while maintaining high output quality. Additional evaluations on NoveltyBench further confirm the generalizability of our approach. Together, our results demonstrate that directly optimizing for creativity within preference frameworks is a promising direction for advancing the creative capabilities of LLMs without compromising output quality.

## 🔍 Abstract (한글 번역)

arXiv:2505.14442v2 발표 유형: 교체-교차  
초록: 대형 언어 모델(LLM)은 자연어 생성 작업에서 인상적인 성능을 보여주었지만, 참신성, 다양성, 놀라움, 품질로 특징지어지는 진정한 창의적 콘텐츠를 생성하는 능력은 여전히 제한적입니다. LLM의 창의성을 향상시키기 위한 기존 방법은 종종 다양성이나 특정 작업에만 좁게 초점을 맞추어, 창의성의 다면적인 본질을 일반화 가능한 방식으로 다루지 못합니다. 본 연구에서는 창의적 선호 최적화(CrPO)라는 새로운 정렬 방법을 제안하여, 모듈식 방식으로 여러 창의성 차원의 신호를 선호 최적화 목표에 주입합니다. 우리는 CrPO와 30개 이상의 심리적 창의성 평가에서 200,000개 이상의 인간 생성 응답과 평가를 포함하는 새로운 대규모 인간 선호 데이터셋인 MuCE를 사용하여 여러 모델의 창의성 강화 버전을 훈련하고 평가합니다. 우리의 모델은 GPT-4o를 포함한 강력한 기준 모델들을 자동 및 인간 평가 모두에서 능가하며, 더 참신하고 다양하며 놀라운 생성물을 생산하면서도 높은 출력 품질을 유지합니다. 추가적인 NoveltyBench 평가에서도 우리의 접근 방식의 일반화 가능성을 더욱 확인합니다. 종합적으로, 우리의 결과는 선호 프레임워크 내에서 창의성을 직접 최적화하는 것이 출력 품질을 손상시키지 않으면서 LLM의 창의적 능력을 발전시키는 유망한 방향임을 보여줍니다.

## 📝 요약

이 연구는 대형 언어 모델(LLM)의 창의적 콘텐츠 생성 능력을 향상시키기 위해 Creative Preference Optimization(CrPO)라는 새로운 정렬 방법을 제안합니다. CrPO는 창의성의 여러 차원을 모듈 방식으로 최적화 목표에 통합하여 모델을 훈련합니다. 연구에서는 30개 이상의 심리학적 창의성 평가를 포함한 20만 개 이상의 인간 생성 응답과 평가를 담은 MuCE 데이터셋을 활용하여 모델을 평가했습니다. 그 결과, 제안된 모델은 GPT-4o를 포함한 강력한 기준 모델들보다 더 새롭고 다양하며 놀라운 결과를 생성하면서도 높은 품질을 유지했습니다. NoveltyBench를 통한 추가 평가에서도 이 접근법의 일반화 가능성이 확인되었습니다. 이는 LLM의 창의적 능력을 향상시키는 데 있어 유망한 방향임을 시사합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 창의적 콘텐츠 생성 능력은 여전히 제한적이다.

- 2. 기존의 LLM 창의성 향상 방법은 다양성이나 특정 작업에 집중하여 창의성의 다면적 특성을 일반화하지 못한다.

- 3. Creative Preference Optimization(CrPO)는 여러 창의성 차원의 신호를 선호도 최적화 목표에 모듈식으로 주입하는 새로운 정렬 방법이다.

- 4. CrPO와 MuCE를 사용한 모델은 GPT-4o를 포함한 강력한 기준 모델보다 더 참신하고 다양하며 놀라운 결과를 생성한다.

- 5. NoveltyBench에서의 추가 평가를 통해 제안된 접근법의 일반화 가능성이 확인되었다.

---

*Generated on 2025-09-22 14:49:26*