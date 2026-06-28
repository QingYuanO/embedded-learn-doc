import { ImageZoom } from 'fumadocs-ui/components/image-zoom';
import { Diagram } from '@/components/mdx/diagram';

interface ImageProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
  className?: string;
}

function resolveRemoteSrc(src: string) {
  if (!src.startsWith('/')) return src;
  const imageHost = process.env.NEXT_PUBLIC_IMAGE_HOST;
  return imageHost ? `https://${imageHost}${src}` : src;
}

export function Image({ src, alt, width, height, className }: ImageProps) {
  if (src.toLowerCase().endsWith('.svg')) {
    return <Diagram src={src} alt={alt} width={width} height={height} className={className} />;
  }

  return (
    <ImageZoom
      src={resolveRemoteSrc(src)}
      alt={alt}
      width={width ?? 750}
      height={height ?? 500}
      priority={false}
    />
  );
}

export { Diagram };
