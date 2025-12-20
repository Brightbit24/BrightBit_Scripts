# import re
# from tkinter import Tk, filedialog
# from docx import Document
# import xml.etree.ElementTree as ET
#
# def create_run_element(text, run):
#     """Return text or nested formatting XML element(s) for a single run."""
#     if not text.strip():
#         return None
#
#     element = None
#     tags = []
#     if run.bold: tags.append("b")
#     if run.italic: tags.append("i")
#     if run.underline: tags.append("u")
#     if run.font.superscript: tags.append("sup")
#     if run.font.subscript: tags.append("sub")
#
#     # Nest tags inside-out
#     for tag in reversed(tags):
#         new_el = ET.Element(tag)
#         if element is not None:
#             new_el.append(element)
#         element = new_el
#
#     if element is None:
#         return text
#     innermost = element
#     while len(innermost):
#         innermost = innermost[0]
#     innermost.text = text
#     return element
#
# def add_formatted_paragraph(frame, tag_name, para):
#     """Adds a <tag_name> with inline formatting to frame (e.g. <p>, <h1>, <h2>)"""
#     node = ET.SubElement(frame, tag_name)
#     prev = None
#     for run in para.runs:
#         part = create_run_element(run.text, run)
#         if part is None:
#             continue
#         if isinstance(part, str):
#             if prev is None:
#                 node.text = (node.text or "") + part
#             else:
#                 prev.tail = (prev.tail or "") + part
#         else:
#             node.append(part)
#             prev = part
#
# def strip_heading_marker(text):
#     return re.sub(r'^<H[12]>\s*', '', text, flags=re.IGNORECASE)
#
# def generate_article_structure_from_docx(docx_path):
#     doc = Document(docx_path)
#     root = ET.Element("article")
#
#     # Empty structure for text-frame-1, 2, 3
#     tf1 = ET.SubElement(root, "text-frame-1")
#     ET.SubElement(tf1, "article-type")
#     ET.SubElement(tf1, "article-title")
#     ET.SubElement(tf1, "authors")
#     ET.SubElement(tf1, "affiliations")
#
#     tf2 = ET.SubElement(root, "text-frame-2")
#     ET.SubElement(tf2, "corresponding-author")
#     ET.SubElement(tf2, "corresponding-author-email")
#     ET.SubElement(tf2, "history")
#     ET.SubElement(tf2, "doi")
#     ET.SubElement(tf2, "qr-code")
#
#     tf3 = ET.SubElement(root, "text-frame-3")
#     ET.SubElement(tf3, "abstract-header")
#     ET.SubElement(tf3, "abstract-content")
#     ET.SubElement(tf3, "keywords")
#
#     # Now populate text-frame-4 with heading and paragraph logic
#     tf4 = ET.SubElement(root, "text-frame-4")
#
#     started = False
#     for para in doc.paragraphs:
#         text = para.text.strip()
#         if not text:
#             continue
#
#         is_h1 = re.match(r'^<H1>', text, re.IGNORECASE)
#         is_h2 = re.match(r'^<H2>', text, re.IGNORECASE)
#
#         if is_h1 or is_h2:
#             started = True
#             para.text = strip_heading_marker(para.text)
#             if is_h1:
#                 add_formatted_paragraph(tf4, "h1", para)
#             else:
#                 add_formatted_paragraph(tf4, "h2", para)
#         elif started:
#             # After H1/H2 has been encountered, add <p> for any regular paragraph
#             add_formatted_paragraph(tf4, "p", para)
#
#     # Add closing HTC tag
#     ET.SubElement(tf4, "htc")
#
#     return root
#
# def main():
#     Tk().withdraw()
#
#     input_path = filedialog.askopenfilename(
#         title="Select DOCX file", filetypes=[("Word Documents", "*.docx")]
#     )
#     if not input_path:
#         print("No DOCX file selected.")
#         return
#
#     output_path = filedialog.asksaveasfilename(
#         title="Save XML As", defaultextension=".xml", filetypes=[("XML Files", "*.xml")]
#     )
#     if not output_path:
#         print("No save path selected.")
#         return
#
#     xml_root = generate_article_structure_from_docx(input_path)
#
#     tree = ET.ElementTree(xml_root)
#     tree.write(output_path, encoding="utf-8", xml_declaration=True)
#     print(f"✅ XML with formatted <text-frame-4> saved to: {output_path}")
#
# if __name__ == "__main__":
#     main()





# import re
# from tkinter import Tk, filedialog
# from docx import Document
# import xml.etree.ElementTree as ET
#
# def create_run_element(text, run):
#     if not text.strip():
#         return None
#
#     element = None
#     tags = []
#     if run.bold: tags.append("b")
#     if run.italic: tags.append("i")
#     if run.underline: tags.append("u")
#     if run.font.superscript: tags.append("sup")
#     if run.font.subscript: tags.append("sub")
#
#     for tag in reversed(tags):
#         new_el = ET.Element(tag)
#         if element is not None:
#             new_el.append(element)
#         element = new_el
#
#     if element is None:
#         return text
#     innermost = element
#     while len(innermost):
#         innermost = innermost[0]
#     innermost.text = text
#     return element
#
# def add_formatted_paragraph(parent, tag_name, para):
#     node = ET.SubElement(parent, tag_name)
#     prev = None
#     for run in para.runs:
#         part = create_run_element(run.text, run)
#         if part is None:
#             continue
#         if isinstance(part, str):
#             if prev is None:
#                 node.text = (node.text or "") + part
#             else:
#                 prev.tail = (prev.tail or "") + part
#         else:
#             node.append(part)
#             prev = part
#
# def strip_heading_marker(text):
#     return re.sub(r'^<H[12]>\s*', '', text, flags=re.IGNORECASE)
#
# def generate_article_structure_from_docx(docx_path):
#     doc = Document(docx_path)
#     root = ET.Element("article")
#
#     # Frames 1–3 (structure only)
#     tf1 = ET.SubElement(root, "text-frame-1")
#     ET.SubElement(tf1, "article-type")
#     ET.SubElement(tf1, "article-title")
#     ET.SubElement(tf1, "authors")
#     ET.SubElement(tf1, "affiliations")
#
#     tf2 = ET.SubElement(root, "text-frame-2")
#     ET.SubElement(tf2, "corresponding-author")
#     ET.SubElement(tf2, "corresponding-author-email")
#     ET.SubElement(tf2, "history")
#     ET.SubElement(tf2, "doi")
#     ET.SubElement(tf2, "qr-code")
#
#     tf3 = ET.SubElement(root, "text-frame-3")
#     ET.SubElement(tf3, "abstract-header")
#     ET.SubElement(tf3, "abstract-content")
#     ET.SubElement(tf3, "keywords")
#
#     # Frame 4 — dynamic content
#     tf4 = ET.SubElement(root, "text-frame-4")
#     started = False
#     in_reference_mode = False
#
#     ref_mode = False
#     ref_counter = 1
#     started = False
#
#     ref_mode = False
#     ref_counter = 1
#     started = False
#
#     for para in doc.paragraphs:
#         text = para.text.strip()
#         if not text:
#             continue
#
#         is_h1 = re.match(r'^<H1>', text, re.IGNORECASE)
#         is_h2 = re.match(r'^<H2>', text, re.IGNORECASE)
#
#         if is_h1 or is_h2:
#             started = True
#             para.text = strip_heading_marker(para.text)
#
#             # ✅ Enter ref mode if heading is References
#             if "references" in para.text.lower():
#                 ref_mode = True
#                 ref_counter = 1
#                 add_formatted_paragraph(tf4, "h1", para)
#                 continue
#
#             # ✅ Exit ref mode on any other heading after References
#             if ref_mode:
#                 ref_mode = False
#
#             if is_h1:
#                 add_formatted_paragraph(tf4, "h1", para)
#             else:
#                 add_formatted_paragraph(tf4, "h2", para)
#
#         elif started:
#             if ref_mode:
#                 ref_el = ET.SubElement(tf4, "ref")
#                 ref_el.text = f"{ref_counter}. "
#                 ref_counter += 1
#
#                 prev = None
#                 for run in para.runs:
#                     part = create_run_element(run.text, run)
#                     if part is None:
#                         continue
#                     if isinstance(part, str):
#                         if prev is None:
#                             ref_el.text += part
#                         else:
#                             prev.tail = (prev.tail or "") + part
#                     else:
#                         ref_el.append(part)
#                         prev = part
#             else:
#                 add_formatted_paragraph(tf4, "p", para)
#
#     ET.SubElement(tf4, "htc")
#     return root
#
# def main():
#     Tk().withdraw()
#
#     input_path = filedialog.askopenfilename(
#         title="Select DOCX file", filetypes=[("Word Documents", "*.docx")]
#     )
#     if not input_path:
#         print("No DOCX file selected.")
#         return
#
#     output_path = filedialog.asksaveasfilename(
#         title="Save XML As", defaultextension=".xml", filetypes=[("XML Files", "*.xml")]
#     )
#     if not output_path:
#         print("No save path selected.")
#         return
#
#     xml_root = generate_article_structure_from_docx(input_path)
#
#     tree = ET.ElementTree(xml_root)
#     tree.write(output_path, encoding="utf-8", xml_declaration=True)
#     print(f"✅ XML with <ref> tagging saved to: {output_path}")
#
# if __name__ == "__main__":
#     main()







# import re
# from tkinter import Tk, filedialog
# from docx import Document
# import xml.etree.ElementTree as ET
#
# def strip_heading_marker(text):
#     return re.sub(r'^<H[12]>\s*', '', text, flags=re.IGNORECASE)
#
# def add_plain_paragraph(parent, tag_name, para):
#     node = ET.SubElement(parent, tag_name)
#     node.set("xml:space", "preserve")
#     node.text = para.text or ""
#
# def generate_article_structure_from_docx(docx_path):
#     doc = Document(docx_path)
#     root = ET.Element("article")
#
#     # text-frame-1
#     tf1 = ET.SubElement(root, "text-frame-1")
#     tags_tf1 = ["article-type", "article-title", "authors", "affiliations"]
#     tf1_elements = {tag: ET.SubElement(tf1, tag) for tag in tags_tf1}
#
#     tf2 = ET.SubElement(root, "text-frame-2")
#     ET.SubElement(tf2, "corresponding-author")
#     ET.SubElement(tf2, "corresponding-author-email")
#     ET.SubElement(tf2, "history")
#     ET.SubElement(tf2, "doi")
#     ET.SubElement(tf2, "qr-code")
#
#     tf3 = ET.SubElement(root, "text-frame-3")
#     ET.SubElement(tf3, "abstract-header")
#     ET.SubElement(tf3, "abstract-content")
#     ET.SubElement(tf3, "keywords")
#
#     tf4 = ET.SubElement(root, "text-frame-4")
#     started = False
#     ref_mode = False
#
#     # Get 2nd to 5th non-empty paragraphs
#     non_empty_paras = [p for p in doc.paragraphs if p.text.strip()]
#     for i, tag in enumerate(tags_tf1):
#         if len(non_empty_paras) > i + 1:
#             para = non_empty_paras[i + 1]
#             tf1_elements[tag].set("xml:space", "preserve")
#             tf1_elements[tag].text = para.text or ""
#
#     # Start adding structured content from <H1> onwards
#     for para in doc.paragraphs:
#         text = para.text.strip()
#         if not text:
#             continue
#
#         is_h1 = re.match(r'^<H1>', text, re.IGNORECASE)
#         is_h2 = re.match(r'^<H2>', text, re.IGNORECASE)
#
#         if is_h1 or is_h2:
#             started = True
#             para.text = strip_heading_marker(para.text)
#
#             if "references" in para.text.lower():
#                 ref_mode = True
#                 add_plain_paragraph(tf4, "h1", para)
#                 continue
#
#             if ref_mode:
#                 ref_mode = False
#
#             if is_h1:
#                 add_plain_paragraph(tf4, "h1", para)
#             else:
#                 add_plain_paragraph(tf4, "h2", para)
#
#         elif started:
#             if ref_mode:
#                 add_plain_paragraph(tf4, "ref", para)
#             else:
#                 add_plain_paragraph(tf4, "p", para)
#
#     ET.SubElement(tf4, "htc")
#     return root
#
# def main():
#     Tk().withdraw()
#
#     input_path = filedialog.askopenfilename(
#         title="Select DOCX file", filetypes=[("Word Documents", "*.docx")]
#     )
#     if not input_path:
#         print("No DOCX file selected.")
#         return
#
#     output_path = filedialog.asksaveasfilename(
#         title="Save XML As", defaultextension=".xml", filetypes=[("XML Files", "*.xml")]
#     )
#     if not output_path:
#         print("No save path selected.")
#         return
#
#     xml_root = generate_article_structure_from_docx(input_path)
#
#     tree = ET.ElementTree(xml_root)
#     tree.write(output_path, encoding="utf-8", xml_declaration=True)
#     print(f"✅ XML saved to: {output_path}")
#
# if __name__ == "__main__":
#     main()


# import re
# import xml.etree.ElementTree as ET
# from xml.dom import minidom
# from tkinter import Tk, filedialog
# from docx import Document
#
#
# def strip_heading_marker(text):
#     return re.sub(r'^<H[12]>\s*', '', text, flags=re.IGNORECASE)
#
#
# def add_formatted_paragraph(parent, tag_name, para):
#     node = ET.SubElement(parent, tag_name)
#     node.set("xml:space", "preserve")
#     prev = None
#     for run in para.runs:
#         part = create_run_element(run.text, run)
#         if part is None:
#             continue
#         if isinstance(part, str):
#             if prev is None:
#                 node.text = (node.text or "") + part
#             else:
#                 prev.tail = (prev.tail or "") + part
#         else:
#             node.append(part)
#             prev = part
#
#
# def generate_article_structure_from_docx(docx_path):
#     doc = Document(docx_path)
#     root = ET.Element("article")
#
#     # text-frame-1
#     tf1 = ET.SubElement(root, "text-frame-1")
#     tags_tf1 = ["article-type", "article-title", "authors", "affiliations"]
#     tf1_elements = {tag: ET.SubElement(tf1, tag) for tag in tags_tf1}
#
#     # text-frame-2
#     tf2 = ET.SubElement(root, "text-frame-2")
#     tf2_tags = {
#         "corresponding-author": ET.SubElement(tf2, "corresponding-author"),
#         "corresponding-author-email": ET.SubElement(tf2, "corresponding-author-email"),
#         "history": ET.SubElement(tf2, "history"),
#         "doi": ET.SubElement(tf2, "doi"),
#         "qr-code": ET.SubElement(tf2, "qr-code")
#     }
#
#     tf3 = ET.SubElement(root, "text-frame-3")
#     abstract_header = ET.SubElement(tf3, "abstract-header")
#     abstract_content = ET.SubElement(tf3, "abstract-content")
#     keywords_node = ET.SubElement(tf3, "keywords")
#     abstract_flag = False
#     next_is_abstract_content = False
#
#     tf4 = ET.SubElement(root, "text-frame-4")
#     htc_node = None  # Will be appended at the end
#
#     # Collect all non-empty paragraphs
#     non_empty_paras = [p for p in doc.paragraphs if p.text.strip()]
#
#     # Fill text-frame-1 (paras 2–5)
#     for i, tag in enumerate(tags_tf1):
#         if len(non_empty_paras) > i + 1:
#             add_formatted_paragraph(tf1, tag, non_empty_paras[i + 1])
#
#     # Fill text-frame-2 and text-frame-4/htc
#     remaining = non_empty_paras[5:]  # Start from 6th paragraph
#     stage = 0
#     for para in remaining:
#         lower_text = para.text.lower()
#         # Check for abstract and keywords in text-frame-3
#         if "abstract" in lower_text and not abstract_flag:
#             abstract_header.set("xml:space", "preserve")
#             abstract_header.text = para.text
#             abstract_flag = True
#             next_is_abstract_content = True
#             continue
#         elif next_is_abstract_content:
#             abstract_content.set("xml:space", "preserve")
#             abstract_content.text = para.text
#             next_is_abstract_content = False
#             continue
#         elif "keywords" in lower_text:
#             keywords_node.set("xml:space", "preserve")
#             keywords_node.text = para.text
#             continue
#
#         if stage == 0:
#             tf2_tags["corresponding-author"].set("xml:space", "preserve")
#             add_formatted_paragraph(tf2, "corresponding-author", para)
#             stage += 1
#         elif stage == 1:
#             tf2_tags["corresponding-author-email"].set("xml:space", "preserve")
#             tf2_tags["corresponding-author-email"].text = para.text
#             stage += 1
#         elif "how to cite this article" in lower_text:
#             htc_node = ET.Element("htc")
#             htc_node.set("xml:space", "preserve")
#             htc_node.text = para.text
#         elif "quick response code" in lower_text:
#             tf2_tags["qr-code"].set("xml:space", "preserve")
#             tf2_tags["qr-code"].text = "Quick Response Code"
#             continue
#         elif tf2_tags["history"].text is None:
#             tf2_tags["history"].set("xml:space", "preserve")
#             tf2_tags["history"].text = para.text
#         elif tf2_tags["doi"].text is None:
#             tf2_tags["doi"].set("xml:space", "preserve")
#             tf2_tags["doi"].text = para.text
#
#     # Frame 4 content: H1/H2 and onward
#     started = False
#     ref_mode = False
#     ref_counter = 1
#
#     for para in doc.paragraphs:
#         text = para.text.strip()
#         if not text:
#             continue
#
#         is_h1 = re.match(r'^<H1>', text, re.IGNORECASE)
#         is_h2 = re.match(r'^<H2>', text, re.IGNORECASE)
#
#         if is_h1 or is_h2:
#             started = True
#             para.text = strip_heading_marker(para.text)
#
#             if "references" in para.text.lower():
#                 ref_mode = True
#                 add_formatted_paragraph(tf4, "h1", para)
#                 continue
#
#             if ref_mode:
#                 ref_mode = False
#
#             if is_h1:
#                 add_formatted_paragraph(tf4, "h1", para)
#             else:
#                 add_formatted_paragraph(tf4, "h2", para)
#
#         elif started:
#             if ref_mode:
#                 ref_el = ET.SubElement(tf4, "ref")
#                 ref_el.set("xml:space", "preserve")
#                 ref_el.text = f"{ref_counter}.\t"
#                 ref_counter += 1
#                 prev = None
#                 for run in para.runs:
#                     part = create_run_element(run.text, run)
#                     if part is None:
#                         continue
#                     if isinstance(part, str):
#                         if prev is None:
#                             ref_el.text += part
#                         else:
#                             prev.tail = (prev.tail or "") + part
#                     else:
#                         ref_el.append(part)
#                         prev = part
#
#
#             else:
#                 add_formatted_paragraph(tf4, "p", para)
#
#     # Ensure <htc> is last in text-frame-4
#     if htc_node is not None:
#         tf4.append(htc_node)
#     else:
#         htc_node = ET.Element("htc")
#         tf4.append(htc_node)
#
#     return root
#
#
# # def prettify_xml(elem):
# #     """Return XML string with each tag on a new line, no indentation."""
# #     rough_string = ET.tostring(elem, encoding="utf-8")
# #     reparsed = minidom.parseString(rough_string)
# #     raw_pretty = reparsed.toprettyxml(indent="")
# #
# #     # Strip leading whitespace from each line
# #     lines = raw_pretty.splitlines()
# #     no_indent_lines = [line.lstrip() for line in lines if line.strip()]
# #     return "\n".join(no_indent_lines)
# def prettify_xml_with_inline_formatting(elem):
#     """Prettify XML and ensure formatting tags are inline."""
#     import re
#     from xml.dom import minidom
#
#     # Step 1: Prettify entire XML using minidom
#     rough_string = ET.tostring(elem, encoding="utf-8")
#     reparsed = minidom.parseString(rough_string)
#     pretty_xml = reparsed.toprettyxml(indent="  ")
#
#     # Step 2: Post-process formatting tags to be inline
#     formatting_tags = ["b", "i", "u", "sup", "sub"]
#
#     for tag in formatting_tags:
#         # Collapse line breaks between formatting tag open/close
#         open_tag_pattern = rf">\s*<{tag}>(.*?)</{tag}>\s*<"
#         pretty_xml = re.sub(open_tag_pattern, lambda m: f">{f'<{tag}>{m.group(1)}</{tag}>'}<", pretty_xml, flags=re.DOTALL)
#
#         # Collapse lines where formatting tag was isolated
#         pretty_xml = re.sub(rf"\n\s*<{tag}>(.*?)</{tag}>\n\s*", rf"<{tag}>\1</{tag}>", pretty_xml, flags=re.DOTALL)
#
#         # Also fix tags that start on a newline and end on another
#         pretty_xml = re.sub(rf"\n\s*<{tag}>(.*?)</{tag}>\n", rf"<{tag}>\1</{tag}>", pretty_xml, flags=re.DOTALL)
#
#     # Finally remove any extra blank lines and strip leading spaces from each line
#     lines = [line.lstrip() for line in pretty_xml.splitlines() if line.strip()]
#     return "\n".join(lines)
#
# def create_run_element(text, run):
#     """Wraps text with formatting tags based on the run."""
#     if not text.strip():
#         return None
#
#     element = None
#     tags = []
#     if run.bold: tags.append("b")
#     if run.italic: tags.append("i")
#     if run.underline: tags.append("u")
#     if run.font.superscript: tags.append("sup")
#     if run.font.subscript: tags.append("sub")
#
#     for tag in reversed(tags):  # Outer tags first
#         new_el = ET.Element(tag)
#         if element is not None:
#             new_el.append(element)
#         element = new_el
#
#     if element is None:
#         return text  # no formatting
#
#     # Set text inside innermost tag
#     innermost = element
#     while len(innermost):
#         innermost = innermost[0]
#     innermost.text = text
#
#     return element
#
#
#
# def main():
#     Tk().withdraw()
#
#     input_path = filedialog.askopenfilename(
#         title="Select DOCX file", filetypes=[("Word Documents", "*.docx")]
#     )
#     if not input_path:
#         print("No DOCX file selected.")
#         return
#
#     output_path = filedialog.asksaveasfilename(
#         title="Save XML As", defaultextension=".xml", filetypes=[("XML Files", "*.xml")]
#     )
#     if not output_path:
#         print("No save path selected.")
#         return
#
#     xml_root = generate_article_structure_from_docx(input_path)
#     pretty_xml = prettify_xml_with_inline_formatting(xml_root)
#
#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(pretty_xml)
#
#     print(f"✅ Pretty-printed XML saved to: {output_path}")
#
#
# if __name__ == "__main__":
#     main()


import re
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog
from docx import Document


def strip_heading_marker(text):
    return re.sub(r'^<H[123]>\s*', '', text, flags=re.IGNORECASE)


def create_run_element(text, run):
    """Wraps text with formatting tags based on the run."""
    # if not text.strip():
    #     return None

    element = None
    tags = []
    if run.bold:
        tags.append("b")
    if run.italic:
        tags.append("i")
    if run.underline:
        tags.append("u")
    if run.font.superscript:
        tags.append("sup")
    if run.font.subscript:
        tags.append("sub")

    for tag in reversed(tags):
        new_el = ET.Element(tag)
        if element is not None:
            new_el.append(element)
        element = new_el

    if element is None:
        return text

    innermost = element
    while len(innermost):
        innermost = innermost[0]
    innermost.text = text
    return element


def add_formatted_paragraph(parent, tag_name, para):
    node = ET.SubElement(parent, tag_name)
    node.set("xml:space", "preserve")
    prev = None
    for run in para.runs:
        part = create_run_element(run.text, run)
        if part is None:
            continue
        if isinstance(part, str):
            if prev is None:
                node.text = (node.text or "") + part
            else:
                prev.tail = (prev.tail or "") + part
        else:
            node.append(part)
            prev = part


def generate_article_structure_from_docx(docx_path):
    doc = Document(docx_path)
    root = ET.Element("article")

    tf1 = ET.SubElement(root, "text-frame-1")
    tf2 = ET.SubElement(root, "text-frame-2")
    tf3 = ET.SubElement(root, "text-frame-3")
    tf4 = ET.SubElement(root, "text-frame-4")

    abstract_header = None
    abstract_content = None
    keywords_node = None
    htc_node = None

    non_empty_paras = [p for p in doc.paragraphs if p.text.strip()]
    # for index,p in enumerate(doc.paragraphs):
    #     print(f"{index}, {p.text}")
    for index,para in enumerate(non_empty_paras):
        print(f"{index}, {para.text}")
    # Frame 1 content
    tags_tf1 = ["article-type", "article-title", "authors", "affiliations"]
    for i, tag in enumerate(tags_tf1):
        if len(non_empty_paras) > i + 1:
            add_formatted_paragraph(tf1, tag, non_empty_paras[i + 1])

    # Frame 2 and 3
    stage = 0
    abstract_flag = False
    collecting_abstract = False
    abstract_content_node = None

    for para in non_empty_paras[5:]:
        lower_text = para.text.lower()

        if not abstract_flag and "abstract" in lower_text:
            add_formatted_paragraph(tf3, "abstract-header", para)
            abstract_flag = True
            collecting_abstract = True
            abstract_content_node = ET.SubElement(tf3, "abstract-content")
            abstract_content_node.set("xml:space", "preserve")
            continue

        if collecting_abstract:
            if lower_text.strip().startswith("keywords"):
                add_formatted_paragraph(tf3, "keywords", para)
                collecting_abstract = False
                continue
            # Add paragraph inside abstract-content as <p>
            p_node = ET.SubElement(abstract_content_node, "p")
            p_node.set("xml:space", "preserve")
            prev = None
            for run in para.runs:
                part = create_run_element(run.text, run)
                if part is None:
                    continue
                if isinstance(part, str):
                    if prev is None:
                        p_node.text = (p_node.text or "") + part
                    else:
                        prev.tail = (prev.tail or "") + part
                else:
                    p_node.append(part)
                    prev = part
            continue

        if stage == 0:
            add_formatted_paragraph(tf2, "corresponding-author", para)
            stage += 1
        elif stage == 1:
            add_formatted_paragraph(tf2, "corresponding-author-email", para)
            stage += 1
        elif "how to cite this article" in lower_text:
            htc_node = ET.Element("htc")
            htc_node.set("xml:space", "preserve")
            htc_node.text = para.text
        elif "quick response code" in lower_text:
            qr = ET.SubElement(tf2, "qr-code")
            qr.set("xml:space", "preserve")
            qr.text = "Quick Response Code"
        elif tf2.find("history") is None:
            add_formatted_paragraph(tf2, "history", para)
        elif tf2.find("doi") is None:
            add_formatted_paragraph(tf2, "doi", para)

    # Frame 4 (main body and references)
    started = False
    ref_mode = False
    ref_counter = 1
    stop_tf4 = False  # NEW: flag to stop after "legends of figures"

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text or stop_tf4:
            continue

        # NEW: Stop processing when "legends of figures" appears
        if (text.lower().strip().startswith("legends of figures")) or (text.lower().strip().startswith("tables")):
            stop_tf4 = True
            continue

        is_h1 = re.match(r'^<H1>', text, re.IGNORECASE)
        is_h2 = re.match(r'^<H2>', text, re.IGNORECASE)
        is_h3 = re.match(r'^<H3>', text, re.IGNORECASE)

        if is_h1 or is_h2 or is_h3:
            started = True
            para.text = strip_heading_marker(para.text)

            if "references" in para.text.lower():
                ref_mode = True
                add_formatted_paragraph(tf4, "h1", para)
                continue

            if ref_mode:
                ref_mode = False

            if is_h1:
                add_formatted_paragraph(tf4, "h1", para)
            elif is_h2:
                add_formatted_paragraph(tf4, "h2", para)
            else:
                add_formatted_paragraph(tf4, "h3", para)

        elif started:
            if ref_mode:
                ref_el = ET.SubElement(tf4, "ref")
                ref_el.set("xml:space", "preserve")
                ref_el.text = f"{ref_counter}.\t"
                ref_counter += 1
                prev = None
                for run in para.runs:
                    part = create_run_element(run.text, run)
                    if part is None:
                        continue
                    if isinstance(part, str):
                        if prev is None:
                            ref_el.text += part
                        else:
                            prev.tail = (prev.tail or "") + part
                    else:
                        ref_el.append(part)
                        prev = part
            else:
                add_formatted_paragraph(tf4, "p", para)

    # Ensure <htc> is last
    if htc_node is not None:
        tf4.append(htc_node)
    else:
        tf4.append(ET.Element("htc"))

    tables_node = ET.SubElement(root, "tables")

    # Find starting point for tables: look for any RUN that is bold and contains "tables" (case-insensitive)
    start_tables_idx = None
    for idx, para in enumerate(doc.paragraphs):
        if any(run.bold and "tables" in run.text.lower() for run in para.runs):
            start_tables_idx = idx + 1
            break

    # Find stop-point: the next "legends of figures" or end of document
    stop_tables_idx = None
    if start_tables_idx is not None:
        for idx in range(start_tables_idx, len(doc.paragraphs)):
            if "legends of figures" in doc.paragraphs[idx].text.lower():
                stop_tables_idx = idx
                break
        if stop_tables_idx is None:
            stop_tables_idx = len(doc.paragraphs)

    if start_tables_idx is not None and stop_tables_idx is not None:
        cur_idx = start_tables_idx
        doc_paras = doc.paragraphs
        while cur_idx < stop_tables_idx:
            para = doc_paras[cur_idx]
            line = para.text.strip()
            if not line:
                cur_idx += 1
                continue

            # Detect if paragraph starts with 'Table X'
            match = re.match(r'^(table\s+\w+.*)', line, re.IGNORECASE)
            if match:
                table_element = ET.SubElement(tables_node, "table")
                header = ET.SubElement(table_element, "header")
                header.text = match.group(1)
                cur_idx += 1

                # Try to find a docx table adjacent to the caption (same logic as before)
                next_table = None
                para_elem = para._element
                for t in doc.tables:
                    parent = para_elem.getparent()
                    siblings = list(parent)
                    idx_of_para = siblings.index(para_elem)
                    if idx_of_para + 1 < len(siblings) and siblings[idx_of_para + 1] is t._element:
                        next_table = t
                        break

                if next_table is not None:
                    # DOCX table found: extract its content
                    for row in next_table.rows:
                        row_elem = ET.SubElement(table_element, "row")
                        seen_cells = set()
                        for cell in row.cells:
                            cell_text = "\n".join([p.text for p in cell.paragraphs if p.text.strip()])
                            if cell_text in seen_cells:
                                continue  # Skip duplicate cells with same text in this row
                            seen_cells.add(cell_text)
                            cell_elem = ET.SubElement(row_elem, "cell")
                            cell_elem.text = cell_text

                else:
                    # No docx Table: Fallback: treat following non-blank lines as table rows until next header/footer
                    row_seek = cur_idx
                    while row_seek < stop_tables_idx:
                        row_para = doc_paras[row_seek]
                        row_line = row_para.text.strip()
                        if re.match(r'^(table\s+\w+)', row_line, re.IGNORECASE) or not row_line:
                            break
                        row_elem = ET.SubElement(table_element, "row")
                        cell_elem = ET.SubElement(row_elem, "cell")
                        cell_elem.text = row_line
                        row_seek += 1
                    cur_idx = row_seek - 1

                # After table: look for one paragraph that does NOT start with "table x" as footer
                footer_idx = cur_idx + 1
                while footer_idx < stop_tables_idx:
                    foot_para = doc_paras[footer_idx]
                    foot_line = foot_para.text.strip()
                    if foot_line == '':
                        footer_idx += 1
                        continue
                    # Not a new table, so it's a footer!
                    if not re.match(r'^(table\s+\w+)', foot_line, re.IGNORECASE):
                        # Accept any type of paragraph here!
                        ET.SubElement(table_element, "footer").text = foot_line
                        cur_idx = footer_idx  # move the cursor forward!
                    break
                # Add this to ensure footer tag exists even if empty
                if table_element.find("footer") is None:
                    footer = ET.SubElement(table_element, "footer")
                    footer.text = ""

            cur_idx += 1

    return root


def write_final_xml_with_inline_formatting(root, output_path):
    """Writes XML with block tags on their own lines (no indent) and formatting tags inline."""

    def serialize_element(elem):
        inline_tags = {"b", "i", "u", "sup", "sub"}
        attrs = " ".join(f'{k}="{v}"' for k, v in elem.attrib.items())
        open_tag = f"<{elem.tag}" + (f" {attrs}" if attrs else "") + ">"
        close_tag = f"</{elem.tag}>"

        # Formatting tags stay inline
        if elem.tag in inline_tags:
            inner = elem.text or ""
            for child in elem:
                inner += serialize_element(child)
                if child.tail:
                    inner += child.tail
            return f"{open_tag}{inner}{close_tag}"

        # Block-level tag: each on its own line
        line = [open_tag]
        if elem.text:
            line[-1] += elem.text

        for child in elem:
            child_str = serialize_element(child)
            line.append(child_str)
            if child.tail:
                line[-1] += child.tail

        line.append(close_tag)
        return "\n".join(line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" ?>\n')
        f.write("<article>\n")
        for child in root:
            f.write(serialize_element(child) + "\n")
        f.write("</article>\n")

def prettify_and_inline_formatting(elem):
    """Prettify XML with no indent and inline formatting tags."""
    import re
    from xml.dom import minidom

    rough_string = ET.tostring(elem, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="")

    # Collapse formatting tags into same line
    inline_tags = ["b", "i", "u", "sup", "sub"]
    for tag in inline_tags:
        pretty_xml = re.sub(
            rf"\n\s*<{tag}>(.*?)</{tag}>\n",
            rf"<{tag}>\1</{tag}>",
            pretty_xml,
            flags=re.DOTALL,
        )
        pretty_xml = re.sub(
            rf"\n\s*<{tag}>(.*?)</{tag}>\s*",
            rf"<{tag}>\1</{tag}>",
            pretty_xml,
            flags=re.DOTALL,
        )

    # Remove indentation from all lines
    lines = [line.lstrip() for line in pretty_xml.splitlines() if line.strip()]
    return "\n".join(lines)


def main():
    from tkinter import Tk, filedialog

    Tk().withdraw()

    input_path = filedialog.askopenfilename(
        title="Select DOCX file", filetypes=[("Word Documents", "*.docx")]
    )
    if not input_path:
        print("No DOCX file selected.")
        return

    output_path = filedialog.asksaveasfilename(
        title="Save XML As", defaultextension=".xml", filetypes=[("XML Files", "*.xml")]
    )
    if not output_path:
        print("No save path selected.")
        return

    xml_root = generate_article_structure_from_docx(input_path)
    pretty_xml = prettify_and_inline_formatting(xml_root)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print(f"✅ Final XML with inline formatting saved to: {output_path}")


if __name__ == "__main__":
    main()


