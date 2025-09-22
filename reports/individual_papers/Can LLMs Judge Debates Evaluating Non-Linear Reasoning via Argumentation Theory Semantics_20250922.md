# Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics

**Korean Title:** LLM이 토론을 평가할 수 있는가? 논증 이론 의미론을 통한 비선형 추론 평가

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Chain-of-Thought|Chain-of-Thought]] [[keywords/specific/In-Context Learning|In-Context Learning]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Computational Argumentation Theory|Computational Argumentation Theory]] [[keywords/unique/Quantitative Argumentation Debate semantics|Quantitative Argumentation Debate semantics]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (85.4% similar) [[2025-09-19/CLEAR_ A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models_20250919|CLEAR: A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models]] (85.4% similar) [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Chain-of-Thought, In-Context Learning
**🔬 Broad Technical**: Large Language Models, Computational Argumentation Theory
**⭐ Unique Technical**: Quantitative Argumentation Debate semantics
## 🔗 유사한 논문
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text]] (85.4% similar)
- [[2025-09-19/CLEAR_ A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models_20250919|CLEAR A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models]] (85.4% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.3% similar)
- [[2025-09-19/Evaluation and Facilitation of Online Discussions in the LLM Era_ A Survey_20250919|Evaluation and Facilitation of Online Discussions in the LLM Era A Survey]] (84.9% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (84.9% similar)


**ArXiv ID**: [2509.15739](https://arxiv.org/abs/2509.15739)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15739.pdf)


**ArXiv ID**: [2509.15739](https://arxiv.org/abs/2509.15739)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15739.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: In-Context Learning, Chain-of-Thought
**⭐ Unique Technical**: Quantitative Argumentation Debate semantics
**🔬 Broad Technical**: Large Language Models, Computational Argumentation Theory

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Computational Argumentation Theory` • 

`Chain-of-Thought` • 

`In-Context Learning` • 

`Quantitative Argumentation Debate semantics`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15739v1 Announce Type: new 
Abstract: Large Language Models (LLMs) excel at linear reasoning tasks but remain underexplored on non-linear structures such as those found in natural debates, which are best expressed as argument graphs. We evaluate whether LLMs can approximate structured reasoning from Computational Argumentation Theory (CAT). Specifically, we use Quantitative Argumentation Debate (QuAD) semantics, which assigns acceptability scores to arguments based on their attack and support relations. Given only dialogue-formatted debates from two NoDE datasets, models are prompted to rank arguments without access to the underlying graph. We test several LLMs under advanced instruction strategies, including Chain-of-Thought and In-Context Learning. While models show moderate alignment with QuAD rankings, performance degrades with longer inputs or disrupted discourse flow. Advanced prompting helps mitigate these effects by reducing biases related to argument length and position. Our findings highlight both the promise and limitations of LLMs in modeling formal argumentation semantics and motivate future work on graph-aware reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15739v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)은 선형 추론 작업에서 뛰어난 성능을 보이지만, 자연 토론에서 발견되는 비선형 구조에 대해서는 아직 충분히 탐구되지 않았습니다. 이러한 비선형 구조는 주로 논증 그래프로 표현됩니다. 우리는 LLMs가 계산 논증 이론(CAT)에서의 구조적 추론을 근사할 수 있는지를 평가합니다. 구체적으로, 우리는 공격 및 지원 관계에 기반하여 논증에 수용 가능성 점수를 할당하는 정량적 논증 토론(QuAD) 의미론을 사용합니다. 두 개의 NoDE 데이터셋에서 대화 형식의 토론만을 제공받은 상태에서, 모델들은 기본 그래프에 접근하지 않고 논증을 순위 매기도록 유도됩니다. 우리는 연쇄적 사고(Chain-of-Thought)와 맥락 내 학습(In-Context Learning)을 포함한 고급 지시 전략 하에 여러 LLMs를 테스트합니다. 모델들은 QuAD 순위와 중간 정도의 일치를 보이지만, 입력이 길어지거나 담론 흐름이 방해받을 경우 성능이 저하됩니다. 고급 프롬프트는 논증 길이와 위치에 관련된 편향을 줄임으로써 이러한 효과를 완화하는 데 도움을 줍니다. 우리의 연구 결과는 LLMs가 형식적 논증 의미론을 모델링하는 데 있어서의 가능성과 한계를 모두 강조하며, 그래프 인식 추론에 대한 향후 연구를 촉진합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 자연 논쟁에서 나타나는 비선형 구조를 얼마나 잘 처리할 수 있는지를 평가합니다. 특히, Computational Argumentation Theory(CAT)의 구조적 추론을 LLM이 근사할 수 있는지를 살펴봅니다. 연구는 QuAD 의미론을 사용하여 논쟁의 공격 및 지원 관계에 따라 수용 가능성 점수를 할당합니다. 두 개의 NoDE 데이터셋에서 대화 형식의 논쟁만을 사용하여, 모델이 기본 그래프 없이도 논쟁을 순위화할 수 있는지를 테스트했습니다. 여러 LLM을 체인 오브 생각(Chain-of-Thought) 및 인컨텍스트 학습(In-Context Learning)과 같은 고급 지시 전략 하에 평가한 결과, 모델은 QuAD 순위와 중간 정도의 일치를 보였으나, 입력이 길어지거나 담론 흐름이 방해받을 때 성능이 저하되었습니다. 고급 프롬프트는 이러한 효과를 완화하여 논쟁 길이와 위치에 따른 편향을 줄이는 데 도움을 주었습니다. 연구는 LLM이 형식적 논증 의미론을 모델링하는 데 있어 가능성과 한계를 동시에 보여주며, 그래프 인식 추론에 대한 향후 연구의 필요성을 제기합니다.

## 🎯 주요 포인트


- 1. 대형 언어 모델(LLMs)은 선형 추론 작업에 뛰어나지만 자연 토론과 같은 비선형 구조에서는 아직 충분히 탐구되지 않았다.

- 2. 본 연구는 LLMs가 계산적 논증 이론(CAT)의 구조적 추론을 근사할 수 있는지를 평가한다.

- 3. QuAD 의미론을 사용하여 LLMs가 그래프 없이 대화 형식의 토론에서 논증을 순위화할 수 있는지를 테스트하였다.

- 4. 고급 프롬프트 전략을 사용하여 논증 길이와 위치에 따른 편향을 줄임으로써 성능 저하를 완화할 수 있었다.

- 5. 연구 결과는 LLMs가 형식적 논증 의미론을 모델링하는 데 있어 가능성과 한계를 모두 보여주며, 그래프 인식 추론에 대한 향후 연구의 필요성을 제기한다.


---

*Generated on 2025-09-22 16:26:58*