import jinja2

PROMPT_JINJA_ENV = jinja2.Environment(autoescape=False, trim_blocks=True, lstrip_blocks=True)


def vision_llm_describe_prompt(page=None):
    content = """
## INSTRUCTION
Transcribe the content from the provided PDF page image into clean Markdown format.

- Only output the content transcribed from the image.
- Do NOT output this instruction or any other explanation.
- If the content is missing or you do not understand the input, return an empty string.

## RULES
1. Do NOT generate examples, demonstrations, or templates.
2. Do NOT output any extra text such as 'Example', 'Example Output', or similar.
3. Do NOT generate any tables, headings, or content that is not explicitly present in the image.
4. Transcribe content word-for-word. Do NOT modify, translate, or omit any content.
5. Do NOT explain Markdown or mention that you are using Markdown.
6. Do NOT wrap the output in ```markdown or ``` blocks.
7. Only apply Markdown structure to headings, paragraphs, lists, and tables, strictly based on the layout of the image. Do NOT create tables unless an actual table exists in the image.
8. Preserve the original language, information, and order exactly as shown in the image.

{% if page %}
At the end of the transcription, add the page divider: `--- Page {{ page }} ---`.
{% endif %}

> If you do not detect valid content in the image, return an empty string.
    """
    template = PROMPT_JINJA_ENV.from_string(content)
    return template.render(page=page)


def vision_llm_figure_describe_prompt():
    content = """
## ROLE
You are an expert visual data analyst.

## GOAL
Analyze the image and provide a comprehensive description of its content. Focus on identifying the type of visual data representation (e.g., bar chart, pie chart, line graph, table, flowchart), its structure, and any text captions or labels included in the image.

## TASKS
1. Describe the overall structure of the visual representation. Specify if it is a chart, graph, table, or diagram.
2. Identify and extract any axes, legends, titles, or labels present in the image. Provide the exact text where available.
3. Extract the data points from the visual elements (e.g., bar heights, line graph coordinates, pie chart segments, table rows and columns).
4. Analyze and explain any trends, comparisons, or patterns shown in the data.
5. Capture any annotations, captions, or footnotes, and explain their relevance to the image.
6. Only include details that are explicitly present in the image. If an element (e.g., axis, legend, or caption) does not exist or is not visible, do not mention it.

## OUTPUT FORMAT (Include only sections relevant to the image content)
- Visual Type: [Type]
- Title: [Title text, if available]
- Axes / Legends / Labels: [Details, if available]
- Data Points: [Extracted data]
- Trends / Insights: [Analysis and interpretation]
- Captions / Annotations: [Text and relevance, if available]

> Ensure high accuracy, clarity, and completeness in your analysis, and include only the information present in the image. Avoid unnecessary statements about missing elements.
    """

    template = PROMPT_JINJA_ENV.from_string(content)
    return template.render()

