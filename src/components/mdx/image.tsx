import { ImageZoom } from 'fumadocs-ui/components/image-zoom';

interface ImageProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
}

export function Image({ src, alt, width, height }: ImageProps) {
  // 如果 src 是相对路径，则添加环境变量中的域名
  let imageSrc = src;
  if (src.startsWith('/')) {
    const imageHost = process.env.NEXT_PUBLIC_IMAGE_HOST;
    if (imageHost) {
      imageSrc = `https://${imageHost}${src}`;
    }
  }
  
  return (
    <ImageZoom 
      src={imageSrc} 
      alt={alt} 
      width={width ?? 750} 
      height={height ?? 500}
      priority={false}
    />
  );
} 