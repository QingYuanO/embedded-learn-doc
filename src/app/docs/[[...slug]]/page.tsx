import { source } from '@/lib/source';
import { DocsPage, DocsBody, DocsDescription, DocsTitle } from 'fumadocs-ui/page';
import { notFound } from 'next/navigation';
import { createRelativeLink } from 'fumadocs-ui/mdx';
import { getMDXComponents } from '@/mdx-components';
import Script from 'next/script';

export default async function Page(props: { params: Promise<{ slug?: string[] }> }) {
  const params = await props.params;
  const page = source.getPage(params.slug);
  if (!page) notFound();

  const MDXContent = page.data.body;

  return (
    <>
      <DocsPage
        toc={page.data.toc}
        full={page.data.full}
        tableOfContent={{
          single: false,
          style: 'clerk',
        }}
      >
        <DocsTitle>{page.data.title}</DocsTitle>
        <DocsDescription>{page.data.description}</DocsDescription>
        <DocsBody>
          <MDXContent
            components={getMDXComponents({
              // this allows you to link to other pages with relative file paths
              a: createRelativeLink(source, page),
            })}
          />
        </DocsBody>
      </DocsPage>
      <Script
        id='giscus'
        src='https://giscus.app/client.js'
        data-repo='QingYuanO/embedded-learn-doc'
        data-repo-id='R_kgDOO6T_Iw'
        data-category='Announcements'
        data-category-id='DIC_kwDOO6T_I84C5DxG'
        data-mapping='url'
        data-strict='0'
        data-reactions-enabled='1'
        data-emit-metadata='0'
        data-input-position='bottom'
        data-theme='preferred_color_scheme'
        data-lang='zh-CN'
        crossOrigin='anonymous'
        async
      ></Script>
    </>
  );
}

export async function generateStaticParams() {
  return source.generateParams();
}

export async function generateMetadata(props: { params: Promise<{ slug?: string[] }> }) {
  const params = await props.params;
  const page = source.getPage(params.slug);
  if (!page) notFound();

  return {
    title: page.data.title,
    description: page.data.description,
  };
}
