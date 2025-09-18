
# Position Bias Mitigates Position Bias:Mitigate Position Bias Through Inter-Position Knowledge Distillation

**Korean Title:** 위치 편향이 위치 편향을 완화시킵니다: 상호 위치 지식 증류를 통해 위치 편향 완화하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Cross-task Generalization|Cross-task Generalization]] [[keywords/broad/Positional Bias|Positional Bias]] [[keywords/broad/Knowledge Distillation|Knowledge Distillation]] [[keywords/specific/Long-context Comprehension|Long-context Comprehension]] [[keywords/unique/Pos2Distill|Pos2Distill]] [[categories/cs.CL|cs.CL]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Long-context Comprehension
**🔬 Broad Technical**: Positional Bias, Knowledge Distillation
**🔗 Specific Connectable**: Contextual Awareness
**⭐ Unique Technical**: Pos2Distill

**ArXiv ID**: [2508.15709](https://arxiv.org/abs/2508.15709)
**Published**: 2025-09-18
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2508.15709.pdf)


## 🏷️ 추출된 키워드



`Positional Bias` • 

`Knowledge Distillation` • 

`Long-context Comprehension` • 

`Pos2Distill` • 

`Cross-task Generalization`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15709v2 Announce Type: replace 
Abstract: Positional bias (PB), manifesting as non-uniform sensitivity across different contextual locations, significantly impairs long-context comprehension and processing capabilities. Previous studies have addressed PB either by modifying the underlying architectures or by employing extensive contextual awareness training. However, the former approach fails to effectively eliminate the substantial performance disparities, while the latter imposes significant data and computational overhead. To address PB effectively, we introduce \textbf{Pos2Distill}, a position to position knowledge distillation framework. Pos2Distill transfers the superior capabilities from advantageous positions to less favorable ones, thereby reducing the huge performance gaps. The conceptual principle is to leverage the inherent, position-induced disparity to counteract the PB itself. We identify distinct manifestations of PB under \textbf{\textsc{r}}etrieval and \textbf{\textsc{r}}easoning paradigms, thereby designing two specialized instantiations: \emph{Pos2Distill-R\textsuperscript{1}} and \emph{Pos2Distill-R\textsuperscript{2}} respectively, both grounded in this core principle. By employing the Pos2Distill approach, we achieve enhanced uniformity and significant performance gains across all contextual positions in long-context retrieval and reasoning tasks. Crucially, both specialized systems exhibit strong cross-task generalization mutually, while achieving superior performance on their respective tasks.

## 🔍 Abstract (한글 번역)

arXiv:2508.15709v2 발표 유형: 대체
요약: 위치 편향(Positional bias, PB)은 서로 다른 문맥적 위치에서 균일하지 않은 감도를 나타내며, 장문 맥락 이해 및 처리 능력을 심각하게 저해합니다. 이전 연구들은 PB를 기존 아키텍처를 수정하거나 광범위한 문맥 인식 훈련을 활용하여 해결해 왔습니다. 그러나 전자의 방법은 상당한 성능 격차를 효과적으로 제거하지 못하며, 후자는 상당한 데이터 및 계산 부담을 가합니다. PB를 효과적으로 해결하기 위해 우리는 \textbf{Pos2Distill}이라는 위치 간 지식 증류 프레임워크를 소개합니다. Pos2Distill은 유리한 위치에서 우수한 능력을 불리한 위치로 전달하여 엄청난 성능 격차를 줄입니다. 개념적 원리는 위치에 의해 유발된 차이를 활용하여 PB 자체를 상쇄하는 것입니다. 우리는 \textbf{\textsc{r}}ecall 및 \textbf{\textsc{r}}easoning 패러다임에서 PB의 구별된 표현을 식별하고, 이 핵심 원리에 기초한 두 가지 전문화된 실체화인 \emph{Pos2Distill-R\textsuperscript{1}} 및 \emph{Pos2Distill-R\textsuperscript{2}}를 설계합니다. Pos2Distill 접근법을 채택함으로써, 우리는 장문 맥락 검색 및 추론 작업에서 모든 문맥적 위치에서 향상된 균일성과 상당한 성능 향상을 달성합니다. 중요한 점은, 두 전문화된 시스템이 상호 강한 교차 작업 일반화를 보여주며, 각각의 작업에서 우수한 성능을 달성합니다.

## 📝 요약

이 논문은 위치 편향(Positional bias, PB)이 긴 문맥 이해 및 처리 능력에 미치는 부정적 영향을 해소하기 위해 Pos2Distill이라는 지식 증류 프레임워크를 제안한다. 이를 통해 유리한 위치에서 덜 유리한 위치로 우수한 능력을 전이시켜 성능 격차를 줄인다. PB의 특징을 파악하여 \textbf{\textsc{r}}etrieval 및 \textbf{\textsc{r}}easoning 패러다임에 대한 두 가지 특화된 시스템을 설계하고 성능을 향상시킨다. Pos2Distill 접근법을 통해 긴 문맥 검색 및 추론 작업에서 모든 위치에서 균일성과 성능 향상을 달성하며, 각각의 작업에서 우수한 성과를 보여준다. 또한, 두 특화된 시스템은 상호 강한 교차 작업 일반화를 보여준다.

## 🎯 주요 포인트


- 1. 위치 편향은 장거리 맥락 이해 및 처리 능력을 심각하게 저해시키며, 이를 해결하기 위해 Pos2Distill이라는 지식 증류 프레임워크를 소개함.

- 2. Pos2Distill은 유리한 위치에서 우월한 능력을 불리한 위치로 이전시켜 성능 격차를 줄이는데 활용됨.

- 3. Pos2Distill은 장거리 검색 및 추론 작업에서 모든 맥락 위치에서 균일성을 향상시키고 성능 향상을 이루어냄.

- 4. Pos2Distill은 각각 Pos2Distill-R^1 및 Pos2Distill-R^2로 설계된 두 가지 특화된 시스템을 통해 위치 편향을 대응하는 핵심 원칙에 기반함.

- 5. 두 특화된 시스템은 상호 강력한 교차 작업 일반화를 보여주며, 각각의 작업에서 우수한 성능을 달성함.


---

*Generated on 2025-09-18 16:55:48*