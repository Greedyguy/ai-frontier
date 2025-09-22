# Catch Me If You Can? Not Yet: LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors

**Korean Title:** "잡을 테면 잡아봐? 아직은 아님: LLM은 여전히 일상 작가들의 암묵적인 글쓰기 스타일을 모방하는 데 어려움을 겪고 있다"

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Zhengxiang Wang|Zhengxiang Wang]] [[authors/Nafis Irtiza Tripto|Nafis Irtiza Tripto]] [[authors/Solha Park|Solha Park]] [[authors/Zhenzhen Li|Zhenzhen Li]] [[authors/Jiawei Zhou|Jiawei Zhou]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Personalized LLM Adaptation

## 🔗 유사한 논문
- [[Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (83.1% similar)
- [[LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.8% similar)
- [[Learning in Context_ Personalizing Educational Content with Large Language Models to Enhance Student Learning_20250919|Learning in Context Personalizing Educational Content with Large Language Models to Enhance Student Learning]] (82.5% similar)
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.3% similar)
- [[Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.2% similar)

## 📋 저자 정보

**Authors:** Zhengxiang Wang, Nafis Irtiza Tripto, Solha Park, Zhenzhen Li, Jiawei Zhou

## 📄 Abstract (원문)

As large language models (LLMs) become increasingly integrated into personal
writing tools, a critical question arises: can LLMs faithfully imitate an
individual's writing style from just a few examples? Personal style is often
subtle and implicit, making it difficult to specify through prompts yet
essential for user-aligned generation. This work presents a comprehensive
evaluation of state-of-the-art LLMs' ability to mimic personal writing styles
via in-context learning from a small number of user-authored samples. We
introduce an ensemble of complementary metrics-including authorship
attribution, authorship verification, style matching, and AI detection-to
robustly assess style imitation. Our evaluation spans over 40000 generations
per model across domains such as news, email, forums, and blogs, covering
writing samples from more than 400 real-world authors. Results show that while
LLMs can approximate user styles in structured formats like news and email,
they struggle with nuanced, informal writing in blogs and forums. Further
analysis on various prompting strategies such as number of demonstrations
reveal key limitations in effective personalization. Our findings highlight a
fundamental gap in personalized LLM adaptation and the need for improved
techniques to support implicit, style-consistent generation. To aid future
research and for reproducibility, we open-source our data and code.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)이 개인의 글쓰기 도구에 점점 더 통합됨에 따라 중요한 질문이 제기됩니다: LLM이 몇 가지 예시만으로도 개인의 글쓰기 스타일을 충실히 모방할 수 있을까요? 개인의 스타일은 종종 미묘하고 암묵적이어서 프롬프트를 통해 명확히 지정하기 어렵지만 사용자에 맞춘 생성에는 필수적입니다. 본 연구는 소수의 사용자가 작성한 샘플을 통해 맥락 내 학습을 통해 개인의 글쓰기 스타일을 모방하는 최첨단 LLM의 능력을 종합적으로 평가합니다. 우리는 스타일 모방을 견고하게 평가하기 위해 저자 속성, 저자 검증, 스타일 매칭, AI 탐지를 포함한 보완적인 메트릭의 앙상블을 소개합니다. 우리의 평가는 뉴스, 이메일, 포럼, 블로그와 같은 도메인 전반에 걸쳐 모델당 40,000개 이상의 생성을 포함하며, 400명 이상의 실제 저자의 글쓰기 샘플을 다룹니다. 결과는 LLM이 뉴스와 이메일과 같은 구조화된 형식에서는 사용자 스타일을 근사할 수 있지만, 블로그와 포럼의 미묘하고 비공식적인 글쓰기에는 어려움을 겪는다는 것을 보여줍니다. 다양한 프롬프트 전략, 예시 수 등의 추가 분석은 효과적인 개인화의 주요 한계를 드러냅니다. 우리의 연구 결과는 개인화된 LLM 적응의 근본적인 격차와 암묵적이고 스타일 일관된 생성을 지원하기 위한 개선된 기술의 필요성을 강조합니다. 향후 연구를 지원하고 재현성을 위해, 우리는 데이터와 코드를 오픈 소스로 제공합니다.

## 📝 요약

이 연구는 대형 언어 모델(LLM)이 소수의 사용자 작성 예시를 통해 개인의 글쓰기 스타일을 모방할 수 있는지를 평가합니다. 이를 위해 저작권 속성, 저작권 검증, 스타일 매칭, AI 탐지 등 다양한 지표를 사용하여 40,000개 이상의 생성물을 분석했습니다. 결과적으로, LLM은 뉴스나 이메일 같은 구조화된 형식에서는 사용자 스타일을 어느 정도 모방할 수 있지만, 블로그나 포럼과 같은 비공식적이고 미묘한 글쓰기에서는 어려움을 겪습니다. 다양한 프롬프트 전략 분석을 통해 개인화의 한계를 밝혔으며, 이는 개인화된 LLM 적응의 근본적인 격차를 시사합니다. 연구의 재현성을 위해 데이터와 코드를 공개했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 개인의 글쓰기 스타일을 몇 가지 예시만으로 충실히 모방할 수 있는지 평가합니다.

- 2. 연구는 저작권 귀속, 저작권 검증, 스타일 매칭, AI 탐지를 포함한 다양한 지표를 통해 스타일 모방 능력을 평가합니다.

- 3. 결과에 따르면 LLM은 뉴스나 이메일과 같은 구조화된 형식에서는 사용자 스타일을 근사할 수 있으나, 블로그나 포럼과 같은 비공식적 글쓰기에서는 어려움을 겪습니다.

- 4. 다양한 프롬프트 전략 분석을 통해 효과적인 개인화에 있어 주요 한계를 드러냅니다.

- 5. 연구의 재현성을 위해 데이터와 코드를 오픈소스로 공개합니다.

---

*Generated on 2025-09-20 05:53:28*