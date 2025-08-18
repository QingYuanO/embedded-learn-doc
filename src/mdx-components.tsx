import defaultMdxComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';
import { Mermaid } from '@/components/mdx/mermaid';
import { Image } from '@/components/mdx/image';
import { R2Link } from '@/components/mdx/R2Link';
import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';
import { Callout } from 'fumadocs-ui/components/callout';
import * as FilesComponents from 'fumadocs-ui/components/files';
import * as TabsComponents from 'fumadocs-ui/components/tabs';
import { FC, ComponentProps } from 'react';
import * as icons from 'lucide-react';
// use this function to get MDX components, you will need it for rendering MDX
export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...(icons as unknown as MDXComponents),
    ...defaultMdxComponents,
    ...TabsComponents,
    ...FilesComponents,
    Accordion,
    Accordions,
    Mermaid,
    Image,
    R2Link,
    blockquote: Callout as unknown as FC<ComponentProps<'blockquote'>>,
    ...components,
  };
}
