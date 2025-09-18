
# Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary

**Korean Title:** 안전 결정 경계의 드러나는 관점에서 LLMs의 과도한 거부 이해 및 완화하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multilingual Scenarios|Multilingual Scenarios]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Safety Decision Boundary|Safety Decision Boundary]] [[keywords/specific/RASS|RASS]] [[keywords/unique/MORBench|MORBench]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multilingual Scenarios
**🔬 Broad Technical**: Large Language Models, Safety Decision Boundary
**🔗 Specific Connectable**: RASS
**⭐ Unique Technical**: MORBench

**ArXiv ID**: [2505.18325](https://arxiv.org/abs/2505.18325)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2505.18325.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Safety Decision Boundaries` • 

`RASS` • 

`MORBench` • 

`Multilingual Scenarios`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18325v3 Announce Type: replace 
Abstract: Large language models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks, yet they often refuse to answer legitimate queries--a phenomenon known as overrefusal. Overrefusal typically stems from over-conservative safety alignment, causing models to treat many reasonable prompts as potentially risky. To systematically understand this issue, we probe and leverage the models' safety decision boundaries to analyze and mitigate overrefusal. Our findings reveal that overrefusal is closely tied to misalignment at these boundary regions, where models struggle to distinguish subtle differences between benign and harmful content. Building on these insights, we present RASS, an automated framework for prompt generation and selection that strategically targets overrefusal prompts near the safety boundary. By harnessing steering vectors in the representation space, RASS efficiently identifies and curates boundary-aligned prompts, enabling more effective and targeted mitigation of overrefusal. This approach not only provides a more precise and interpretable view of model safety decisions but also seamlessly extends to multilingual scenarios. We have explored the safety decision boundaries of various LLMs and construct the MORBench evaluation set to facilitate robust assessment of model safety and helpfulness across multiple languages. Code and datasets are available at https://github.com/Master-PLC/RASS.

## 🔍 Abstract (한글 번역)

arXiv:2505.18325v3 발표 유형: 대체
요약: 대형 언어 모델(LLMs)은 다양한 작업 영역에서 놀라운 능력을 보여주었지만 종종 합법적인 쿼리에 대답을 거부하는 현상인 과도한 거부(overrefusal)가 발생합니다. 과도한 거부는 일반적으로 너무 보수적인 안전 정렬에서 비롯되어 모델이 많은 합리적인 프롬프트를 잠재적으로 위험한 것으로 취급하게 만듭니다. 이 문제를 체계적으로 이해하기 위해 우리는 모델의 안전 결정 경계를 조사하고 활용하여 과도한 거부를 분석하고 완화하는 데 노력했습니다. 우리의 연구 결과는 과도한 거부가 이러한 경계 영역에서의 불일치와 밀접하게 관련되어 있음을 밝혀내었으며, 모델이 양성과 해로운 콘텐츠 간의 미묘한 차이를 구별하는 데 어려움을 겪는 곳입니다. 이러한 통찰력을 기반으로 우리는 RASS를 제안합니다. 이는 과도한 거부 프롬프트를 안전 경계 근처에서 전략적으로 대상화하는 프롬프트 생성 및 선택을 자동화하는 프레임워크입니다. 표현 공간에서 스티어링 벡터를 활용하여 RASS는 효율적으로 경계에 정렬된 프롬프트를 식별하고 선별하여 과도한 거부를 보다 효과적으로 대응할 수 있게 합니다. 이 접근 방식은 모델의 안전 결정에 대한 더 정확하고 해석 가능한 시각을 제공할 뿐만 아니라 다국어 시나리오로 신속하게 확장될 수 있습니다. 우리는 다양한 LLMs의 안전 결정 경계를 탐색하고 MORBench 평가 세트를 구축하여 다국어에서 모델의 안전성과 유용성을 견고하게 평가할 수 있도록 지원합니다. 코드 및 데이터셋은 https://github.com/Master-PLC/RASS에서 사용할 수 있습니다.

## 📝 요약

최근 대형 언어 모델(Large language models, LLMs)은 다양한 작업에서 놀라운 성능을 보여주지만 종종 합리적인 질문에 답변을 거부하는 현상, 즉 과도한 거부(overrefusal)가 발생합니다. 이 연구는 LLMs의 안전 결정 경계를 조사하여 과도한 거부를 분석하고 완화하는 자동 프레임워크인 RASS를 제안합니다. 연구 결과는 과도한 거부가 모델이 유해한 콘텐츠와 유해하지 않은 콘텐츠를 구별하는 데 어려움을 겪는 경계 영역의 불일치와 밀접하게 관련되어 있음을 보여줍니다. RASS는 표현 공간에서 조향 벡터를 활용하여 경계에 정렬된 프롬프트를 효율적으로 식별하고 선별하여 과도한 거부를 더 효과적으로 완화합니다. 이 방법론은 모델의 안전 결정에 대한 보다 정확하고 해석 가능한 시각을 제공할 뿐만 아니라 다국어 시나리오로도 자연스럽게 확장될 수 있습니다. 이 연구는 다양한 LLMs의 안전 결정 경계를 탐색하고 다국어 환경에서 모델의 안전성과 유용성을 견고하게 평가하기 위한 MORBench 평가 세트를 구축했습니다. 해당 코드와 데이터셋은 https://github.com/Master-PLC/RASS에서 확인할 수 있습니다.

## 🎯 주요 포인트


- 대형 언어 모델은 다양한 작업에서 놀라운 능력을 보여주지만 종종 합리적인 쿼리에 대답을 거부하는 현상인 overrefusal이 발생한다.

- overrefusal은 모델이 많은 합리적인 프롬프트를 잠재적으로 위험한 것으로 취급하도록 하는 과도한 보수적 안전 정렬에서 비롯된다.

- overrefusal은 모델이 유해한 콘텐츠와 유해하지 않은 콘텐츠 사이의 미묘한 차이를 구별하는 데 어려움을 겪는 경계 영역에서 발생하는 것으로 나타났다.


---

*Generated on 2025-09-18 16:27:10*