
# Radiology Report Conditional 3D CT Generation with Multi Encoder Latent diffusion Model

**Korean Title:** 방사선 보고서 조건부 3D CT 생성: 다중 인코더 잠재 확산 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi Encoder Text Conditioning

## 🔗 유사한 논문
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (82.6% similar)
- [[DICE Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction]] (79.9% similar)
- [[Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (79.8% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (78.9% similar)
- [[Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14780v1 Announce Type: new 
Abstract: Text to image latent diffusion models have recently advanced medical image synthesis, but applications to 3D CT generation remain limited. Existing approaches rely on simplified prompts, neglecting the rich semantic detail in full radiology reports, which reduces text image alignment and clinical fidelity. We propose Report2CT, a radiology report conditional latent diffusion framework for synthesizing 3D chest CT volumes directly from free text radiology reports, incorporating both findings and impression sections using multiple text encoder. Report2CT integrates three pretrained medical text encoders (BiomedVLP CXR BERT, MedEmbed, and ClinicalBERT) to capture nuanced clinical context. Radiology reports and voxel spacing information condition a 3D latent diffusion model trained on 20000 CT volumes from the CT RATE dataset. Model performance was evaluated using Frechet Inception Distance (FID) for real synthetic distributional similarity and CLIP based metrics for semantic alignment, with additional qualitative and quantitative comparisons against GenerateCT model. Report2CT generated anatomically consistent CT volumes with excellent visual quality and text image alignment. Multi encoder conditioning improved CLIP scores, indicating stronger preservation of fine grained clinical details in the free text radiology reports. Classifier free guidance further enhanced alignment with only a minor trade off in FID. We ranked first in the VLM3D Challenge at MICCAI 2025 on Text Conditional CT Generation and achieved state of the art performance across all evaluation metrics. By leveraging complete radiology reports and multi encoder text conditioning, Report2CT advances 3D CT synthesis, producing clinically faithful and high quality synthetic data.

## 🔍 Abstract (한글 번역)

arXiv:2509.14780v1 발표 유형: 신규  
초록: 텍스트에서 이미지로의 잠재 확산 모델은 최근 의료 이미지 합성에서 발전을 이루었지만, 3D CT 생성에 대한 응용은 여전히 제한적입니다. 기존 접근 방식은 간소화된 프롬프트에 의존하여 전체 방사선 보고서의 풍부한 의미론적 세부 사항을 간과함으로써 텍스트 이미지 정렬과 임상적 충실도를 감소시킵니다. 우리는 방사선 보고서 조건부 잠재 확산 프레임워크인 Report2CT를 제안하여, 여러 텍스트 인코더를 사용하여 소견 및 인상 섹션을 통합하여 자유 텍스트 방사선 보고서로부터 직접 3D 흉부 CT 볼륨을 합성합니다. Report2CT는 세 가지 사전 학습된 의료 텍스트 인코더(BiomedVLP CXR BERT, MedEmbed, ClinicalBERT)를 통합하여 미세한 임상적 맥락을 포착합니다. 방사선 보고서와 복셀 간격 정보는 CT RATE 데이터셋의 20000개의 CT 볼륨에서 훈련된 3D 잠재 확산 모델을 조건화합니다. 모델 성능은 실제 합성 분포 유사성을 위한 Frechet Inception Distance (FID)와 의미론적 정렬을 위한 CLIP 기반 지표를 사용하여 평가되었으며, GenerateCT 모델과의 추가적인 질적 및 양적 비교가 이루어졌습니다. Report2CT는 해부학적으로 일관된 CT 볼륨을 우수한 시각적 품질과 텍스트 이미지 정렬로 생성했습니다. 다중 인코더 조건화는 CLIP 점수를 개선하여 자유 텍스트 방사선 보고서의 세밀한 임상 세부 사항 보존을 강화함을 나타냈습니다. 분류기 없는 가이던스는 FID에서의 약간의 트레이드오프만으로 정렬을 더욱 향상시켰습니다. 우리는 MICCAI 2025에서 열린 VLM3D 챌린지의 텍스트 조건부 CT 생성 부문에서 1위를 차지했으며, 모든 평가 지표에서 최첨단 성능을 달성했습니다. 완전한 방사선 보고서와 다중 인코더 텍스트 조건화를 활용함으로써, Report2CT는 3D CT 합성을 발전시켜 임상적으로 충실하고 고품질의 합성 데이터를 생성합니다.

## 📝 요약

Report2CT는 자유 텍스트 형태의 방사선 보고서를 기반으로 3D 흉부 CT 영상을 생성하는 프레임워크로, 기존의 단순한 프롬프트에 의존하는 방법론을 개선했습니다. 이 모델은 BiomedVLP CXR BERT, MedEmbed, ClinicalBERT 등 세 개의 사전 학습된 의료 텍스트 인코더를 활용하여 임상적 맥락을 세밀하게 반영합니다. 20,000개의 CT 데이터셋을 활용하여 훈련된 이 모델은 Frechet Inception Distance(FID)와 CLIP 기반 지표로 평가되었으며, GenerateCT 모델과 비교하여 뛰어난 해부학적 일관성과 시각적 품질을 보여주었습니다. 또한, VLM3D Challenge에서 1위를 차지하며, 모든 평가 지표에서 최첨단 성능을 달성했습니다. Report2CT는 방사선 보고서의 전체 내용을 활용하여 임상적으로 충실하고 고품질의 합성 데이터를 생성하는 데 기여합니다.

## 🎯 주요 포인트

- 1. Report2CT는 자유 텍스트 형태의 방사선 보고서로부터 3D 흉부 CT 볼륨을 합성하는 방사선 보고서 조건부 잠재 확산 프레임워크를 제안합니다.

- 2. 이 모델은 BiomedVLP CXR BERT, MedEmbed, ClinicalBERT 등 세 가지 사전 학습된 의료 텍스트 인코더를 통합하여 세밀한 임상 문맥을 포착합니다.

- 3. Report2CT는 20000개의 CT 볼륨 데이터셋을 기반으로 훈련되었으며, Frechet Inception Distance (FID)와 CLIP 기반 메트릭을 사용하여 모델 성능을 평가했습니다.

- 4. 다중 인코더 조건부 설정은 CLIP 점수를 개선하여 방사선 보고서의 세밀한 임상 세부사항 보존을 강화했습니다.

- 5. MICCAI 2025의 VLM3D 챌린지에서 Text Conditional CT Generation 부문 1위를 차지하며 모든 평가 지표에서 최첨단 성능을 달성했습니다.

---

*Generated on 2025-09-19 16:06:49*