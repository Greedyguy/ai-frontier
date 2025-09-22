
# Large Language Model probabilities cannot distinguish between possible and impossible language

**Korean Title:** 대형 언어 모델의 확률은 가능한 언어와 불가능한 언어를 구별할 수 없습니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Minimal-pair Surprisal

## 🔗 유사한 논문
- [[Language Models Identify Ambiguities and Exploit Loopholes]] (85.9% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (84.3% similar)
- [[Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary]] (83.0% similar)
- [[Explicit Reasoning Makes Better Judges A Systematic Study on Accuracy, Efficiency, and Robustness]] (82.8% similar)
- [[Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (82.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15114v1 Announce Type: new 
Abstract: A controversial test for Large Language Models concerns the ability to discern possible from impossible language. While some evidence attests to the models' sensitivity to what crosses the limits of grammatically impossible language, this evidence has been contested on the grounds of the soundness of the testing material. We use model-internal representations to tap directly into the way Large Language Models represent the 'grammatical-ungrammatical' distinction. In a novel benchmark, we elicit probabilities from 4 models and compute minimal-pair surprisal differences, juxtaposing probabilities assigned to grammatical sentences to probabilities assigned to (i) lower frequency grammatical sentences, (ii) ungrammatical sentences, (iii) semantically odd sentences, and (iv) pragmatically odd sentences. The prediction is that if string-probabilities can function as proxies for the limits of grammar, the ungrammatical condition will stand out among the conditions that involve linguistic violations, showing a spike in the surprisal rates. Our results do not reveal a unique surprisal signature for ungrammatical prompts, as the semantically and pragmatically odd conditions consistently show higher surprisal. We thus demonstrate that probabilities do not constitute reliable proxies for model-internal representations of syntactic knowledge. Consequently, claims about models being able to distinguish possible from impossible language need verification through a different methodology.

## 🔍 Abstract (한글 번역)

arXiv:2509.15114v1 발표 유형: 신규  
초록: 대형 언어 모델에 대한 논란이 되는 테스트는 가능한 언어와 불가능한 언어를 구별하는 능력에 관한 것입니다. 일부 증거는 문법적으로 불가능한 언어의 한계를 넘는 것에 대한 모델의 민감성을 증명하지만, 이 증거는 테스트 자료의 타당성에 대한 이유로 논란이 있습니다. 우리는 모델 내부 표현을 사용하여 대형 언어 모델이 '문법적-비문법적' 구분을 나타내는 방식을 직접 탐구합니다. 새로운 벤치마크에서, 우리는 4개의 모델에서 확률을 도출하고 최소 쌍의 놀람 차이를 계산하여 문법적 문장에 할당된 확률을 (i) 낮은 빈도의 문법적 문장, (ii) 비문법적 문장, (iii) 의미적으로 이상한 문장, (iv) 화용론적으로 이상한 문장에 할당된 확률과 비교합니다. 예측은 문자열 확률이 문법의 한계를 나타내는 대리자로 기능할 수 있다면, 비문법적 조건이 언어적 위반을 포함하는 조건들 중에서 두드러지게 나타나며 놀람 비율에 급증을 보일 것이라는 것입니다. 우리의 결과는 비문법적 제시에 대한 독특한 놀람 서명을 드러내지 않으며, 의미적 및 화용론적으로 이상한 조건들이 일관되게 더 높은 놀람을 보입니다. 따라서 확률은 구문 지식의 모델 내부 표현에 대한 신뢰할 수 있는 대리자가 아님을 입증합니다. 결과적으로, 모델이 가능한 언어와 불가능한 언어를 구별할 수 있다는 주장은 다른 방법론을 통해 검증이 필요합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 가능한 언어와 불가능한 언어를 구분할 수 있는 능력을 평가하는 논란의 여지가 있는 테스트를 다룹니다. 기존 연구에서는 모델이 문법적으로 불가능한 언어를 감지할 수 있다고 주장했지만, 테스트 자료의 타당성에 대한 논란이 있었습니다. 본 연구는 모델 내부 표현을 사용하여 '문법적-비문법적' 구분을 직접 탐구합니다. 새로운 벤치마크를 통해 4개의 모델에서 확률을 추출하고, 문법적 문장과 (i) 낮은 빈도의 문법적 문장, (ii) 비문법적 문장, (iii) 의미적으로 이상한 문장, (iv) 실용적으로 이상한 문장에 할당된 확률을 비교했습니다. 결과적으로, 비문법적 조건이 다른 언어적 위반 조건보다 높은 놀람 값을 보여야 한다는 예측과 달리, 의미적 및 실용적 이상 조건이 일관되게 더 높은 놀람 값을 보였습니다. 이는 확률이 모델의 구문 지식 표현을 신뢰할 수 있는 대리자로 작용하지 않음을 시사하며, 모델이 가능한 언어와 불가능한 언어를 구분할 수 있다는 주장은 다른 방법론을 통해 검증이 필요함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델이 문법적으로 불가능한 언어를 구별할 수 있는 능력에 대한 테스트의 타당성이 논란이 되고 있습니다.

- 2. 모델 내부 표현을 통해 '문법적-비문법적' 구분을 직접적으로 탐구하는 새로운 벤치마크를 제시했습니다.

- 3. 4개의 모델에서 확률을 유도하고 최소 쌍 놀람 차이를 계산하여 문법적 문장과 다양한 언어적 위반 조건을 비교했습니다.

- 4. 연구 결과, 비문법적 조건이 특별한 놀람 패턴을 보이지 않았으며, 의미적 및 실용적으로 이상한 조건이 더 높은 놀람을 나타냈습니다.

- 5. 따라서, 모델이 가능한 언어와 불가능한 언어를 구별할 수 있다는 주장은 다른 방법론을 통해 검증이 필요합니다.

---

*Generated on 2025-09-19 15:54:55*