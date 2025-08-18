interface R2LinkProps {
  src: string;
  target?: string;
  className?: string;
  children: React.ReactNode;
}

export function R2Link({ src, target, className, children }: R2LinkProps) {
  // 如果 src 是相对路径，则添加环境变量中的域名
  let imageSrc = src;
  if (src.startsWith('/')) {
    const imageHost = process.env.NEXT_PUBLIC_IMAGE_HOST;
    if (imageHost) {
      imageSrc = `https://${imageHost}${src}`;
    }
  }

  return (
    <a href={imageSrc} target={target} className={className}>
      {children}
    </a>
  );
}
