'use client';

import { useEffect, useId, useState } from 'react';
import { cn } from '@/lib/utils';

interface DiagramProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
  className?: string;
}

function resolveDiagramSrc(src: string) {
  if (!src.startsWith('/')) return src;
  if (src.startsWith('/electronic-components/')) return src;
  const imageHost = process.env.NEXT_PUBLIC_IMAGE_HOST;
  return imageHost ? `https://${imageHost}${src}` : src;
}

/** 内联 SVG，使 .dark 主题 CSS 变量能作用于图形内部 */
export function Diagram({ src, alt, width, height, className }: DiagramProps) {
  const uid = useId().replace(/:/g, '');
  const [svg, setSvg] = useState('');
  const imageSrc = resolveDiagramSrc(src);

  useEffect(() => {
    let cancelled = false;

    fetch(imageSrc)
      .then((res) => {
        if (!res.ok) throw new Error(`Failed to load diagram: ${imageSrc}`);
        return res.text();
      })
      .then((raw) => {
        if (cancelled) return;

        const patched = raw
          .replace(/<svg\b/, '<svg class="ec-diagram-svg"')
          .replace(/\bid="([^"]+)"/g, `id="$1-${uid}"`)
          .replace(/url\(#([^)]+)\)/g, `url(#$1-${uid})`);

        setSvg(patched);
      })
      .catch((err) => {
        console.error(err);
      });

    return () => {
      cancelled = true;
    };
  }, [imageSrc, uid]);

  return (
    <figure
      className={cn(
        'ec-diagram mx-auto my-4 max-w-full rounded-lg border border-border bg-card p-3',
        className
      )}
      style={width ? { maxWidth: width } : undefined}
      role='img'
      aria-label={alt}
    >
      {svg ? (
        <div dangerouslySetInnerHTML={{ __html: svg }} />
      ) : (
        <div
          className='animate-pulse rounded-md bg-muted'
          style={{ width: width ?? '100%', height: height ?? 200 }}
          aria-hidden
        />
      )}
      <figcaption className='sr-only'>{alt}</figcaption>
    </figure>
  );
}
