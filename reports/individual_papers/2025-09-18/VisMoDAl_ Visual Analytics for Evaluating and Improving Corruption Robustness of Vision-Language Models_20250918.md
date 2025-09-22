# VisMoDAl: Visual Analytics for Evaluating and Improving Corruption Robustness of Vision-Language Models

**Korean Title:** VisMoDAl: 비전-언어 모델의 부패 견고성을 평가하고 개선하기 위한 시각적 분석

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Huanchen Wang|Huanchen Wang]] [[authors/Wencheng Zhang|Wencheng Zhang]] [[authors/Zhiqiang Wang|Zhiqiang Wang]] [[authors/Zhicong Lu|Zhicong Lu]] [[authors/Yuxin Ma|Yuxin Ma]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Corruption Robustness

## 🔗 유사한 논문
- [[Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (81.2% similar)
- [[V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (80.2% similar)
- [[UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (80.2% similar)
- [[ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (79.5% similar)
- [[MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (79.1% similar)

## 📋 저자 정보

**Authors:** Huanchen Wang, Wencheng Zhang, Zhiqiang Wang, Zhicong Lu, Yuxin Ma

## 📄 Abstract (원문)

Vision-language (VL) models have shown transformative potential across
various critical domains due to their capability to comprehend multi-modal
information. However, their performance frequently degrades under distribution
shifts, making it crucial to assess and improve robustness against real-world
data corruption encountered in practical applications. While advancements in VL
benchmark datasets and data augmentation (DA) have contributed to robustness
evaluation and improvement, there remain challenges due to a lack of in-depth
comprehension of model behavior as well as the need for expertise and iterative
efforts to explore data patterns. Given the achievement of visualization in
explaining complex models and exploring large-scale data, understanding the
impact of various data corruption on VL models aligns naturally with a visual
analytics approach. To address these challenges, we introduce VisMoDAl, a
visual analytics framework designed to evaluate VL model robustness against
various corruption types and identify underperformed samples to guide the
development of effective DA strategies. Grounded in the literature review and
expert discussions, VisMoDAl supports multi-level analysis, ranging from
examining performance under specific corruptions to task-driven inspection of
model behavior and corresponding data slice. Unlike conventional works,
VisMoDAl enables users to reason about the effects of corruption on VL models,
facilitating both model behavior understanding and DA strategy formulation. The
utility of our system is demonstrated through case studies and quantitative
evaluations focused on corruption robustness in the image captioning task.

## 🔍 Abstract (한글 번역)

비전-언어(VL) 모델은 다중 모달 정보를 이해할 수 있는 능력 덕분에 다양한 중요한 분야에서 변혁적인 잠재력을 보여주고 있습니다. 그러나 이러한 모델의 성능은 분포 변화에 따라 자주 저하되며, 실질적인 응용에서 직면하는 현실 세계의 데이터 손상에 대한 강인성을 평가하고 개선하는 것이 중요합니다. VL 벤치마크 데이터셋과 데이터 증강(DA)의 발전이 강인성 평가와 개선에 기여했지만, 모델 행동에 대한 심층적인 이해 부족과 데이터 패턴 탐색을 위한 전문 지식 및 반복적인 노력이 필요하다는 도전 과제가 남아 있습니다. 복잡한 모델을 설명하고 대규모 데이터를 탐색하는 데 있어 시각화의 성과를 고려할 때, 다양한 데이터 손상이 VL 모델에 미치는 영향을 이해하는 것은 시각적 분석 접근 방식과 자연스럽게 일치합니다. 이러한 도전 과제를 해결하기 위해, 우리는 VisMoDAl이라는 시각적 분석 프레임워크를 소개합니다. 이 프레임워크는 다양한 손상 유형에 대한 VL 모델의 강인성을 평가하고, 효과적인 DA 전략 개발을 안내하기 위해 성능이 저하된 샘플을 식별합니다. 문헌 검토와 전문가 논의를 기반으로 한 VisMoDAl은 특정 손상 하에서의 성능 검토부터 모델 행동과 해당 데이터 슬라이스의 과제 중심 검사에 이르기까지 다층 분석을 지원합니다. 전통적인 작업과 달리, VisMoDAl은 사용자가 VL 모델에 대한 손상의 영향을 추론할 수 있게 하여 모델 행동 이해와 DA 전략 수립을 촉진합니다. 우리 시스템의 유용성은 이미지 캡셔닝 작업에서의 손상 강인성에 초점을 맞춘 사례 연구와 정량적 평가를 통해 입증됩니다.

## 📝 요약

Vision-language(VL) 모델은 다중 모달 정보를 이해하는 능력 덕분에 다양한 분야에서 혁신적인 잠재력을 보여주고 있습니다. 그러나 실제 데이터 손상에 대한 강건성을 평가하고 개선하는 것이 중요합니다. 이를 해결하기 위해 VisMoDAl이라는 시각적 분석 프레임워크를 소개합니다. VisMoDAl은 VL 모델의 다양한 손상 유형에 대한 강건성을 평가하고, 성능이 저하된 샘플을 식별하여 효과적인 데이터 증강(DA) 전략 개발을 지원합니다. 이 시스템은 특정 손상에 대한 성능 분석부터 모델 행동 및 데이터 조각에 대한 심층 분석까지 다층적인 분석을 제공합니다. VisMoDAl은 이미지 캡셔닝 작업에서의 손상 강건성에 초점을 맞춘 사례 연구와 정량적 평가를 통해 그 유용성을 입증합니다.

## 🎯 주요 포인트

- 1. Vision-language 모델은 다중 모달 정보를 이해하는 능력 덕분에 다양한 분야에서 혁신적인 잠재력을 보여주고 있습니다.

- 2. 실제 데이터 손상에 대한 강건성을 평가하고 개선하는 것이 중요하며, 이를 위해 VL 벤치마크 데이터셋과 데이터 증강 기법이 기여하고 있습니다.

- 3. VisMoDAl은 다양한 손상 유형에 대한 VL 모델의 강건성을 평가하고, 효과적인 데이터 증강 전략 개발을 위한 시각 분석 프레임워크입니다.

- 4. VisMoDAl은 특정 손상 하에서의 성능 평가부터 모델 행동과 데이터 조각에 대한 과제 중심의 검사까지 다중 수준의 분석을 지원합니다.

- 5. VisMoDAl의 유용성은 이미지 캡셔닝 작업에서의 손상 강건성에 초점을 맞춘 사례 연구와 정량적 평가를 통해 입증되었습니다.

---

*Generated on 2025-09-20 05:51:49*