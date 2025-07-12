import defaultMdxComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';
import { Mermaid } from '@/components/mdx/mermaid';
import { ImageZoom } from 'fumadocs-ui/components/image-zoom';
import { Image } from '@/components/mdx/image';
// use this function to get MDX components, you will need it for rendering MDX
export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    Mermaid,
    Image,
    img: (props) => {
      return <ImageZoom {...props} />;
    },
    ...components,
  };
}
