https://learn.getgrav.org/15/content/markdown

https://support.typora.io/Markdown-Reference/

---
Here's an example(code enbeded):


```     
function test() {
  console.log("notice the blank line before this function?");
}
```



syntax highlighting(code enbeded):
```ruby                     
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

single line embeded

`single line embeded`


math function

$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$

Table

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |


Text size

# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Headings
###### h6 Heading
<!--
This is a comment
-->
___
***

Lorem ipsum dolor sit amet, graecis denique ei vel, at duo primis mandamus. Et legere ocurreret pri, animal tacimates complectitur ad cum. Cu eum inermis inimicus efficiendi. Labore officiis his ex, soluta officiis concludaturque ei qui, vide sensibus vim ad.
___
<div class="class">
    This is <b>HTML</b>
</div>
**rendered as bold text**

_rendered as italicized text_

~~Strike through this text.~~

* valid bullet
- valid bullet
+ valid bullet

+ Lorem ipsum dolor sit amet
+ Consectetur adipiscing elit
+ Integer molestie lorem at massa
+ Facilisis in pretium nisl aliquet
+ Nulla volutpat aliquam velit
  - Phasellus iaculis neque
  - Purus sodales ultricies
  - Vestibulum laoreet porttitor sem
  - Ac tristique libero volutpat at
+ Faucibus porta lacus fringilla vel
+ Aenean sit amet erat nunc
+ Eget porttitor lorem

1. Lorem ipsum dolor sit amet

2. Consectetur adipiscing elit

3. Integer molestie lorem at massa

4. Facilisis in pretium nisl aliquet

5. Nulla volutpat aliquam velit

6. Faucibus porta lacus fringilla vel

7. Aenean sit amet erat nunc


> **Fusion Drive** combines a hard drive with a flash storage (solid-state drive) and presents it as a single logical volume with the space of both drives combined.
Renders to:

Fusion Drive combines a hard drive with a flash storage (solid-state drive) and presents it as a single logical volume with the space of both drives combined.

and this HTML:

<blockquote>
  <p><strong>Fusion Drive</strong> combines a hard drive with a flash storage (solid-state drive) and presents it as a single logical volume with the space of both drives combined.</p>
  </blockquote>
  ￼Copy


  Blockquotes can also be nested:
  > Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue.
  Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi.
  >> Sed adipiscing elit vitae augue consectetur a gravida nunc vehicula. Donec auctor
  odio non est accumsan facilisis. Aliquam id turpis in dolor tincidunt mollis ac eu diam.


