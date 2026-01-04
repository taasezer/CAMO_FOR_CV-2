import { useEffect, useState } from 'react';
import axios from 'axios';
import { ScanEye, Box } from 'lucide-react';

interface Detection {
    label: string;
    confidence: number;
}

export function DetectionList() {
    const [detections, setDetections] = useState<Detection[]>([]);
    const [isScanning, setIsScanning] = useState(false);
    const [scannedText, setScannedText] = useState<string[]>([]);

    useEffect(() => {
        const interval = setInterval(() => {
            axios.get('http://localhost:8000/ai/detections')
                .then(res => setDetections(res.data.detections))
                .catch(err => console.error(err));
        }, 500); // Update every 500ms

        return () => clearInterval(interval);
    }, []);

    const handleScanText = async () => {
        setIsScanning(true);
        try {
            const res = await axios.post('http://localhost:8000/ai/scan-text');
            setScannedText(res.data.text);
        } catch (error) {
            console.error(error);
        } finally {
            setIsScanning(false);
        }
    };

    return (
        <div className="bg-card border border-border rounded-xl p-4 flex flex-col gap-4 h-full">
            <div className="flex items-center justify-between">
                <h3 className="font-semibold flex items-center gap-2">
                    <Box className="w-5 h-5 text-primary" />
                    Detected Objects
                </h3>
                <span className="text-xs text-muted-foreground animate-pulse">Live</span>
            </div>

            <div className="flex-1 overflow-y-auto min-h-[100px] space-y-2">
                {detections.length === 0 ? (
                    <p className="text-sm text-muted-foreground italic">No objects detected...</p>
                ) : (
                    detections.map((d, i) => (
                        <div key={i} className="flex justify-between items-center bg-secondary/50 p-2 rounded text-sm">
                            <span className="font-medium capitalize">{d.label}</span>
                            <span className="text-xs text-muted-foreground">{(d.confidence * 100).toFixed(0)}%</span>
                        </div>
                    ))
                )}
            </div>

            <div className="pt-4 border-t border-border">
                <h3 className="font-semibold flex items-center gap-2 mb-2">
                    <ScanEye className="w-5 h-5 text-blue-500" />
                    OCR Scanner
                </h3>
                <button
                    onClick={handleScanText}
                    disabled={isScanning}
                    className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg flex items-center justify-center gap-2 text-sm font-medium transition-colors disabled:opacity-50"
                >
                    {isScanning ? 'Scanning...' : 'Scan Label Text'}
                </button>

                {scannedText.length > 0 && (
                    <div className="mt-3 p-2 bg-secondary/30 rounded text-xs font-mono space-y-1">
                        {scannedText.map((line, i) => (
                            <p key={i}>{line}</p>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}
