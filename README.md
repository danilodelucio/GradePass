![cover_v5](https://github.com/user-attachments/assets/310c16e7-2176-4ae6-bbea-c2b4fc2e35ec)

> _Artwork [Solas (Dragon Age)](https://www.artstation.com/artwork/P66RP8), by [Leticia Matsuoka](https://leticiamatsuoka.com/)._

# Quick Access 🔗
- [Introduction](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#introduction-)
- [How to Use](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#how-to-use-)
- [Light Groups](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#light-groups)
- [Installing](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#installing-%EF%B8%8F)
- [Nuke Compatibility](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#nuke-compatibility-%EF%B8%8F)
- [Troubleshooting](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#troubleshooting-%EF%B8%8F)
- [Support me](https://github.com/danilodelucio/GradePass?tab=readme-ov-file#support-me-)

---

# Introduction 📝
The **GradePass** node is designed to grade render passes directly without needing to extract them. It uses the subtractive method, and you can view and tweak the selected AOV in one single node.

It contains the same knobs as the Grade node, along with Hue Rotation, Saturation and some extra features.

![Screenshot 2024-11-26 203647](https://github.com/user-attachments/assets/44bfe902-7b61-4f73-a59e-9fa0efec1c69)

> [!IMPORTANT]
> _This node does not address **NaN**/**Infinite** values or perform complex calculations to fix AOV issues._

# How to Use 📖

<h2>Viewer - Final Result</h2>

- It allows you to check the final result while you adjust the selected AOV;

![final_result_v1_](https://github.com/user-attachments/assets/8d15b4f2-42ff-4564-b049-a703e5471a7b)

<h2>Viewer - Solo AOV</h2>

- It allows you to isolate and check what passes you want to work on (similar to the **Shuffle** node);

![solo_aov_v3_](https://github.com/user-attachments/assets/d43e4d47-ad80-49e6-8e91-b1bc4223a1da)

- You can use it along with the **Disable Adjustments** option to disable all the changes while you check the selected AOV;

![disable_adjustments_v2_](https://github.com/user-attachments/assets/b7e70805-1a90-4938-b155-3c1444ae3994)

<h2>Viewer - All Layers</h2>

- Display all the AOVs from the input node (similar to the **LayerContactSheet** node);

![final_result_v1_](https://github.com/user-attachments/assets/4879331f-abb0-4fce-9622-f69b4e8715c2)

- You can stack the **GradePass** nodes with all the AOV changes you have done;

![stack_v1_](https://github.com/user-attachments/assets/983e4494-feaa-4ac1-944e-8b1d7d055223)

# Light Groups

- **GradePass** also works with **Light Groups**, so you can control their intensities individually;

![light_groups_v1_](https://github.com/user-attachments/assets/f1fc9bb1-326d-4cb1-8e78-d72a70dd5fd0)

# Nuke Compatibility ☢️

- The **GradePass** node was created in **Nuke 12.1v5**, but it's designed to work on any Nuke version, including Commercial, Non-Commercial and Indie.

# Installing ⚙️

- You can download all the content by clicking on the green button, then **Download Zip**;

![image](https://github.com/user-attachments/assets/4fd1b030-6d93-4b15-8d88-c9f661d75119)

- Drag and drop the **GradePass.nk** file into your Nuke;

![drag_and_drop_v1_](https://github.com/user-attachments/assets/c34836d9-6ce5-48e2-a581-66c01a640cb6)

- Alternatively, you can click on the **GradePass.nk** file here on GitHub -> `Copy Raw file` button, then paste it into your Nuke;

![copy_raw_v1_](https://github.com/user-attachments/assets/62d294f1-52b2-4dcd-a8b4-871c4db128eb)

# Troubleshooting 🛠️

If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/GradePass/discussions) page and create a **New Discussion**.

For bugs, please go to the [Issues](https://github.com/danilodelucio/GradePass/issues) page and create a **New Issue**.

# Supporters 💪
-

# Support me! 🥺

![image](https://github.com/user-attachments/assets/271b46ae-183f-4918-8e11-14b3cbf0fb5b)

This personal project required significant time and extra hours of hard work to make it available to everyone.

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://buymeacoffee.com/danilodelucio). ☕

> _If you donate any amount, please mention this tool (also your preference name if you want to), so your name will appear in the **Supporters** list above._

You can also share this tool or send me a positive message, it would help me in the same way.

---

Special thanks to Gustavo Goncalves, Marco Silva, Leticia Matsuoka and Wesley Junior for testing this tool and providing valuable feedback for improvement.

# Cheers! 🥂
