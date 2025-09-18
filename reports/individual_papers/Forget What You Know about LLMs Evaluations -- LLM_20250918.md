
# Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon

**Korean Title:** LLM 평가에 대해 알고 있던 것을 잊어버리세요 - LLM은 카멜레온과 같습니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Resilience in LLM Evaluation|Resilience in LLM Evaluation]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Benchmark Overfit Detector|Benchmark Overfit Detector]] [[keywords/specific/Meta-evaluation Framework|Meta-evaluation Framework]] [[keywords/unique/Chameleon Benchmark Overfit Detector|Chameleon Benchmark Overfit Detector]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Meta-evaluation Framework
**🔬 Broad Technical**: Large Language Models, Benchmark Evaluation
**🔗 Specific Connectable**: Chameleon Benchmark Overfit Detector
**⭐ Unique Technical**: C-BOD

**ArXiv ID**: [2502.07445](https://arxiv.org/abs/2502.07445)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2502.07445.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Benchmark Overfit Detector` • 

`MMLU benchmark` • 

`Chameleon Benchmark Overfit Detector (C-BOD` • 

`Resilience in LLM evaluation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.07445v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) often appear to excel on public benchmarks, but these high scores may mask an overreliance on dataset-specific surface cues rather than true language understanding. We introduce the Chameleon Benchmark Overfit Detector (C-BOD), a meta-evaluation framework that systematically distorts benchmark prompts via a parametric transformation and detects overfitting of LLMs. By rephrasing inputs while preserving their semantic content and labels, C-BOD exposes whether a model's performance is driven by memorized patterns. Evaluated on the MMLU benchmark using 26 leading LLMs, our method reveals an average performance degradation of 2.15% under modest perturbations, with 20 out of 26 models exhibiting statistically significant differences. Notably, models with higher baseline accuracy exhibit larger performance differences under perturbation, and larger LLMs tend to be more sensitive to rephrasings, indicating that both cases may overrely on fixed prompt patterns. In contrast, the Llama family and models with lower baseline accuracy show insignificant degradation, suggesting reduced dependency on superficial cues. Moreover, C-BOD's dataset- and model-agnostic design allows easy integration into training pipelines to promote more robust language understanding. Our findings challenge the community to look beyond leaderboard scores and prioritize resilience and generalization in LLM evaluation.

## 🔍 Abstract (한글 번역)

arXiv:2502.07445v2 발표 유형: replace-cross
요약: 대형 언어 모델 (LLMs)은 종종 공개 벤치마크에서 우수한 성과를 보이지만, 이러한 높은 점수는 실제 언어 이해보다는 데이터셋 특정 표면 단서에 지나치게 의존할 수 있다. 우리는 카멜레온 벤치마크 오버피팅 탐지기 (C-BOD)를 소개합니다. 이는 벤치마크 프롬프트를 매개변수 변환을 통해 체계적으로 왜곡하고 LLMs의 오버피팅을 감지하는 메타평가 프레임워크입니다. 입력을 다시 표현하면서 의미 콘텐츠와 레이블을 보존함으로써, C-BOD는 모델의 성능이 기억된 패턴에 의해 주도되는지 여부를 드러냅니다. 26개의 주요 LLM을 사용하여 MMLU 벤치마크에서 평가한 결과, 우리의 방법은 적은 변형에서 2.15%의 평균 성능 저하를 보여주며, 26개 중 20개의 모델이 통계적으로 유의미한 차이를 나타냅니다. 특히, 높은 기준 정확도를 가진 모델은 변형에 대해 더 큰 성능 차이를 보이며, 큰 LLM은 다시 표현에 더 민감할 가능성이 있어서 둘 다 고정된 프롬프트 패턴에 지나치게 의존할 수 있다는 것을 나타냅니다. 반면, Llama 패밀리와 기준 정확도가 낮은 모델은 무의미한 저하를 보여주어 표면적인 단서에 대한 의존성이 줄어들었다고 제안합니다. 더욱이, C-BOD의 데이터셋 및 모델에 중립적인 디자인은 훈련 파이프라인에 쉽게 통합되어 더 견고한 언어 이해를 촉진합니다. 우리의 연구 결과는 커뮤니티에게 리더보드 점수를 넘어서 LLM 평가에서 탄력성과 일반화를 우선시하도록 도전합니다.

## 📝 요약

초대형 언어 모델은 공개 벤치마크에서 뛰어난 성적을 보이지만, 이는 실제 언어 이해가 아닌 데이터셋 특정 표면 단서에 지나치게 의존할 수 있다. 본 연구에서는 Chameleon Benchmark Overfit Detector (C-BOD)를 소개하여 벤치마크 프롬프트를 왜곡하고 LLM의 오버피팅을 감지하는 메타평가 프레임워크를 제시한다. MMLU 벤치마크를 사용하여 26개의 주요 LLM을 평가한 결과, 우리의 방법은 적은 왜곡으로 평균 성능 하락률이 2.15%이며, 26개 모델 중 20개가 통계적으로 유의미한 차이를 보였다. 더 큰 기본 정확도를 가진 모델일수록 왜곡에 민감하며, 큰 LLM일수록 다시 표현에 민감할 것으로 나타났다. 이에 반해, Llama 패밀리와 낮은 기본 정확도를 가진 모델은 중요하지 않은 하락을 보여 얕은 단서에 대한 의존성이 줄어든 것으로 나타났다. 또한, C-BOD의 데이터셋 및 모델에 대한 디자인은 훈련 파이프라인에 쉽게 통합되어 더 견고한 언어 이해를 촉진한다. 우리의 연구 결과는 리더보드 점수를 넘어서 LLM 평가에서 탄력성과 일반화를 우선시해야 함을 도전한다.

## 🎯 주요 포인트


- 대형 언어 모델은 공개 벤치마크에서 우수한 성과를 보이지만 이는 데이터셋 특정 표면 단서에 지나치게 의존할 수 있음

- Chameleon Benchmark Overfit Detector (C-BOD)는 벤치마크 프롬프트를 왜곡시켜 LLM의 오버피팅을 감지하는 메타평가 프레임워크를 소개

- C-BOD는 모델의 성능이 암기된 패턴에 의해 주도되는지 노출시키며, 대부분의 모델이 통계적으로 유의미한 차이를 보임

- 더 큰 LLM일수록 rephrasing에 민감할 가능성이 높으며, Llama 패밀리 및 낮은 기준 성능을 보이는 모델은 표면적인 단서에 대한 의존성이 줄어들었다고 제안함

- C-BOD는 데이터셋 및 모델에 중립적인 설계로 강건한 언어 이해를 촉진하기 위해 훈련 파이프라인에 쉽게 통합될 수 있음.


---

*Generated on 2025-09-18 16:31:00*